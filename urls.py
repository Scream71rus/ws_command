
from handlers.chat_handler import ChatHandler


urls = [
    (r'/api/?', ChatHandler,),
]
