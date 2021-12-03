from locust import HttpUser, between, task
class ApiUser(HttpUser):
    # wait_time = between(2, 5)
    # def on_start(self):
    #     self.client.post("/login", {
    #         "username":"admin", 
    #         "password":"admin1234"
    #     })
    # we create 20 user and spawn rate is 1000/sec
    # after the server can't handle so many requests, we would remove the server's ip and port url from database
    @task(1)
    def profile(self):
        self.client.get('/')
