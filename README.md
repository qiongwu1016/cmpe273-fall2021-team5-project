# Implement Circuit Breaker in Proxy Server 

Team 5:
1. Qiong Wu
2. Lingxiang Hu
3. Yu Qiu
4. Dylan Zhang
  
  
## Installation
- Programming
  - flask
  - pymongo
  - CircuitBreaker

- Testing
  - Postman
  - Locust

## Runbook
### Preparation

1. 
  - run app.py

![app1](screenshots/app1.png)
  - response
  
![app1res](screenshots/app1res.png)

2. 
  - run app1.py

![app2](screenshots/app2.png)

  - response
 
![app2](screenshots/app2res.png)

3. run proxyserver.py

![proxyserver](screenshots/proxyserver.png)

4. 
  - run client.py (locust) with http://0.0.0.0:8089

![locust](screenshots/locust.png)

  - setup number of users and spawn rate after locust run sucessful 

![locustsetup](screenshots/locustsetup.png)

### Testing Result

1. Postman 
  - sucess retrieved from server

![postmanres1](screenshots/postmanres1.png)

![postmanres2](screenshots/postmanres2.png)

  - failed from server
 
![postmanresfailed](screenshots/postmanresfailed.png)

2. Locust
  - sucess retrieved response with green line and failed request with red line

![locustres](screenshots/locustres.png)

3. Log
  - Log printed in terminal to show failed server being removed or added back
  ![image](https://user-images.githubusercontent.com/70813818/144513753-7a591c04-bbd5-444a-8411-fd7e4f468f04.png)
