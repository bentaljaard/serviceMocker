import tornado.ioloop
import tornado.web
from core.endpoint_handler import EndpointHandler
from core.mock_dispatcher import MockDispatcher



def register_app(dispatcher):
	return tornado.web.Application([
		(r"/.*", EndpointHandler, {"dispatcher":dispatcher})
	])

if __name__=="__main__":
	
	dispatcher = MockDispatcher("../mocks")
	app = register_app(dispatcher)
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()