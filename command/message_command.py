
from models.message_model import MessageModel

class Command:
	def execute(self, data):
		raise NotImplementedError()

	def cancel(self):
		raise NotImplementedError()

	def name(self):
		raise NotImplementedError()

class CreateMessage(Command):

    async def execute(self, data):
        data, errors = await MessageModel.create(data)
        if errors is None:
            return {'ok': True, 'data': data}
        else:
            return {'ok': False, 'errors': errors}

    async def name(self):
        return "createMessage"

class GetMessage(Command):

    async def execute(self, data):
        data = await MessageModel.get(data.get('limit'))
        return {'ok': True, 'data': data}

    async def name(self):
        return "getMessages"