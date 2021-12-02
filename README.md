# Implement Circuit Breaker in Proxy Server 

Team 4:
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

