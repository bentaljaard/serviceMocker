import tornado.web
import re
from models.mock_request import MockRequest 
from core.mock_dispatcher import MockDispatcher
from tornado import gen

class EndpointHandler(tornado.web.RequestHandler):

	def initialize(self, dispatcher):
		self.dispatcher = dispatcher

	def get(self):
		self.handle_endpoint()

	def post(self):
		self.handle_endpoint()

	def put(self):
		self.handle_endpoint()

	def patch(self):
		self.handle_endpoint()

	def delete(self):
		self.handle_endpoint()

	def head(self):
		self.handle_endpoint()
		
	def options(self):
		self.handle_endpoint()

	def handle_endpoint(self):
		# load request into dict
		# details = dict()
		# details["endpoint"] = self.request.uri
		# details["method"] = self.request.method
		# # details["valid_endpoint"] = self.is_valid_endpoint(self.request.uri)
		# details["query"] = self.request.query
		# details["headers"] = dict(self.request.headers)
		# details["body"] = self.request.body.decode("utf-8")
		# details["arguments"] = {k: v[0].decode('utf8') for k, v in self.request.arguments.items()}
		# details["query_arguments"] = {k: v[0].decode('utf8') for k, v in self.request.query_arguments.items()}
		# details["body_arguments"] = self.request.body_arguments
		# print(details)

		# response = self.dispatcher.get_response(self.to_mapper_request())
		if len(self.dispatcher.get_mock(self.to_mapper_request())) > 0:
			mock = self.dispatcher.get_mock(self.to_mapper_request())[0]
			if not mock.assert_body(self.to_mapper_request()):
				raise tornado.web.HTTPError(400)
			else:
				response = mock.response
		else:
			response = None
		if not response:
			raise tornado.web.HTTPError(404)
		else:
			for k, v in response.headers.items():
				self.set_header(k,v)
			self.write(response.body_response())


	def to_mapper_request(self):
	    dic = {"method": self.request.method,
	           "url": self.request.uri,
	           "headers": dict(self.request.headers),
	           "body": self.request.body.decode("utf-8")}

	    return MockRequest(dic)