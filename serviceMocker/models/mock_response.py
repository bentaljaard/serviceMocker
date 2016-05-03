import json


class MockResponse(object):

    def __init__(self, response_dic):
        self.response_dic = response_dic

        self.setup_status()
        self.setup_body()
        self.setup_headers()

    def setup_status(self):
        self.status = self.response_dic["status"] if "status" in self.response_dic else 200

    def setup_body(self):
        self.body = BodyResponse(self.response_dic)

    def setup_headers(self):
        self.headers = self.response_dic.get("headers", {})
    

    def body_response(self):
        return self.body.read_value()

    def headers(self):
        return self.headers


class BodyResponse(object):

    @property
    def body_type(self):
        return self._body_type

    def __init__(self, dic):
        self.value = ""
        self._body_type = BodyResponse.NONE

        if "body" in dic:
            self._body_type = BodyResponse.RAW
            self.set_from_object(dic["body"])

        

    def read_value(self):
        return self.value()

    
    def set_from_object(self, object):
        if isinstance(object, str):
            self.value = lambda: str(object).encode('utf8')

        elif isinstance(object, dict) or isinstance(object, list):
            self.value = lambda: json.dumps(object).encode('utf8')

   
   

    RAW = "raw"
    IMAGE = "image"
    FILE = "file"
    NONE = "none"
