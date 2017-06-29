__version__ ='0.1'

import tornado.ioloop
import tornado.web
from core.endpoint_handler import EndpointHandler
from core.mock_dispatcher import MockDispatcher
import argparse



def register_app(dispatcher):
	return tornado.web.Application([
		(r"/.*", EndpointHandler, {"dispatcher":dispatcher})
	])

if __name__=="__main__":
	
	parser = argparse.ArgumentParser(prog='serviceMocker',description="serviceMocker allows you to specify mocks using simple configuration")
	parser.add_argument('--port', '-p', help='Specify the listening port for your mock server', default=8888)
	parser.add_argument('--folder', '-f', help='Specify the folder that will be containing the mock service definitions', required=True)
	parser.add_argument('--version', action='version', version='%(prog)s '+ __version__, help='Print the serviceMocker version')
	args = parser.parse_args()
	
	dispatcher = MockDispatcher(args.folder)
	app = register_app(dispatcher)
	app.listen(args.port)
	tornado.ioloop.IOLoop.current().start()