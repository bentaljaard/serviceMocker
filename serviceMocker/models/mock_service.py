from .mock_request import MockRequest
from .mock_response import MockResponse
from os.path import basename
import os


class MockService(object):

    def __init__(self, dic, file_name):
        self.request = MockRequest(dic["request"])
        self.response = MockResponse(dic["response"])
        self.file_name = file_name
        self.display_name = self.get_display_name(dic, file_name)

    def get_display_name(self, dic, file_name):
        if "name" in dic:
            return dic["name"]
        else:
            return os.path.splitext(basename(file_name))[0]

    def handles_request(self, other_request):
        return self.request == other_request
