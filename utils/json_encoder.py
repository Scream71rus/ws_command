
from bson import ObjectId
import datetime
import json

class ObjectEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime.datetime) or \
                 isinstance(o, datetime.date):

            return datetime.datetime.strftime(o, "%Y-%m-%d %H:%M")

        if isinstance(o, ObjectId):
            return str(o)

        return json.JSONEncoder.default(self, o)
