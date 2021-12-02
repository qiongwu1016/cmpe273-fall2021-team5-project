from locust import HttpUser, between, task
class ApiUser(HttpUser):
    # wait_time = between(2, 5)
    # def on_start(self):
    #     self.client.post("/login", {
    #         "username":"admin", 
    #         "password":"admin1234"
    #     })
    @task(1)
    def profile(self):
        self.client.get('/')
