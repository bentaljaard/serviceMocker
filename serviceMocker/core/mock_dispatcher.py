import yaml
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from models.mock_service import MockService
import os


class MockDispatcher(object):

    def __init__(self, mock_path):
        self.mock_path = mock_path
        self.parse_mock()
        self.install_watchers()

    def parse_mock(self):
        self.yaml_files = get_yaml_files(self.mock_path)
        self.mocks = list(map(self.create_mock_service, self.yaml_files))
        for mock in self.mocks:
            print('Loaded mock service: ' + mock.display_name)

    def create_mock_service(self, yml_file):
        full_path = self.mock_path + "/" + yml_file
        # read yaml file into mock service
        with open(full_path, "r") as file:
            return MockService(yaml.load(file), full_path)

    def get_response(self, request):
        return [mock.response for mock in self.mocks if mock.handles_request(request)]


    def get_mock(self, request):
        return [mock for mock in self.mocks if mock.handles_request(request)]
        #TODO: expand to check if body value can be asserted, ie. handles request, but body matching fails

    def install_watchers(self):
        self.event_handler = MockDirectoryListener(self)
        self.install_watcher(self.mock_path)

    def install_watcher(self, path):
        observer = Observer()
        observer.schedule(self.event_handler, path, recursive=True)
        observer.start()


class MockDirectoryListener(FileSystemEventHandler):

    def __init__(self, mock_loader):
        self.mock_loader = mock_loader

    def on_any_event(self, event): 
        print('Event triggered on filesystem: ' + event.event_type)
        self.mock_loader.parse_mock()
       


def get_yaml_files(path):
    files = os.listdir(path)
    return filter(lambda file: re.match(".*\.yaml$", file), files)
