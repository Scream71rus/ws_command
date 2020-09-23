
import datetime

from cerberus import Validator
from models.base_model import BaseModel

CREATE_SCHEMA = {
    'command': {'type': 'string', 'required': True},
    'userName': {'type': 'string', 'required': True},
    'text': {'type': 'string', 'required': True},
}


class MessageModel(BaseModel):

    @classmethod
    async def get(cls, limit=None):
        cursor = cls.db.message.find().sort('created')
        result = await cursor.to_list(length=limit)

        return result

    @classmethod
    async def create(cls, data):
        v = Validator(CREATE_SCHEMA)

        if v.validate(data):
            data['created'] = datetime.datetime.now()
            await cls.db.message.insert_one(data)

            return data, None

        else:
            return data, v.errors


