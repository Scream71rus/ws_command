
import sys
import os

sys.path.append(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), '.'))

import urls
import asyncio

import logging
import tornado.web
import tornado.platform.asyncio
import tornado.log
from tornado.options import define, options, parse_config_file
import motor.motor_asyncio

from models.base_model import BaseModel


define("port", type=int)
define("db_name", type=str)
define("db_host", type=str)
define("db_port", type=int)
define("debug", type=str)


parse_config_file("application.conf")
tornado.options.parse_command_line()


class Application(tornado.web.Application):

    @property
    def db(self):
        return self._db

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        self._db_client = motor.motor_asyncio.AsyncIOMotorClient(
            host=options.db_host, port=options.db_port)
        self._db = self._db_client[options.db_name]

        BaseModel.db = self.db


if __name__ == '__main__':
    tornado.log.enable_pretty_logging()

    logging_mode = logging.DEBUG if options.debug == 'yes' else logging.INFO
    tornado.log.app_log.setLevel(logging_mode)

    tornado.platform.asyncio.AsyncIOMainLoop().install()

    application = Application(
        urls.urls,
        debug=(True if options.debug == "yes" else False))

    application.listen(options.port)
    asyncio.get_event_loop().run_forever()
