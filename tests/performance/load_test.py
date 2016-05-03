from locust import HttpLocust, TaskSet, task

class MockTestSet(TaskSet):
    @task(2)
    def jsonmock(self):
        self.client.get("/text")

    @task(1)
    def xmlmock(self):
        self.client.get("/xml")

class MyLocust(HttpLocust):
    task_set = MockTestSet
    min_wait = 2000
    max_wait = 5000
