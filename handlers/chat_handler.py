
from handlers.base_handler import BaseHandler
from command.message_command import *


COMMANDS = {'createMessage': CreateMessage(), 'getMessages': GetMessage()}


class ChatHandler(BaseHandler):

    async def get(self):
        self.render('../templates/index.html')

    async def post(self):
        command = self.request_data.get('command')
        data = await COMMANDS.get(command).execute(self.request_data)

        self.response(data)