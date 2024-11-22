# Better Docker Voting App

- this is a modified version of [dockers official voting app](https://github.com/dockersamples/example-voting-app) 
- when i started working on this i found some things difficult so had to do some adjustment in original code 
- updated images are available in my [docker repo](https://hub.docker.com/repository/docker/luffyxxsenpai/voting/general)
---
### this is a voting application using 4 microservice 
1. Vote: A frontend application where users can vote for their preferred option.
2. Worker: A backend service that processes votes stored in Redis and moves them to a PostgreSQL database.
3. Redis: An in-memory data store used to temporarily store votes.
4. Result: A frontend application that displays the real-time voting results.

---
## IMAGE GUIDE
- all the required images are in the same repo
- pull all the tags (vote, worker, result)

- vote:     http://localhost:8080
- result:   http://localhost:8081

- ### VOTE
- this is the frontend of voting app
- Running on: http://localhost:8080
- Default values of these envs are also mentioned 
```
Environment Variables required:
  - OPTION_A: Cats
  - OPTION_B: Dogs
  - REDIS_HOST: redis
  - REDIS_PORT: 6379
  - REDIS_DB: 0
```

- ### worker
- this fetches data from redis and filter it and save it to postgres db
- would suggest you to make a postgres user and a database instead of default one 
```
- Environment Variables and Default Values:
POSTGRES_HOST = db
POSTGRES_USER = postgres
POSTGRES_PASSWORD = postgres
POSTGRES_DATABASE = postgres
REDIS_HOST = redis
REDIS_PORT = 6379
REDIS_DB = 0
```
- ### result
- this is a frontend to show the result of votes
- it will fetch data from postgres and reflect on [website](http://localhost:8081) 
```
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DATABASE
```
---
## running using docker run

1. vote : `docker run --network=host -p 8080:8080 -e REDIS_HOST=127.0.0.1 luffyxxsenpai/voting:vote`

2. worker: `docker run --network=host -e REDIS_HOST=127.0.0.1 -e REDIS_PORT=6379 -e POSTGRES_USER=postgres -e POSTGRES_DATABASE=postgres -e POSTGRES_HOST=127.0.0.1 -e POSTGRES_PORT=5432 luffyxxsenpai/voting:worker`

3. result: `docker run --network=host -e POSTGRES_USER=postgres -e POSTGRES_HOST=127.0.0.1 -e POSTGRES_DATABASE=postgres -e POSTGRES_PORT=5432 luffyxxsenpai/voting:result`

4. i am using postgres and redis locally for testing it with docker, just start a redis and postgres server locally 
---

## running using docker-compose

**soon**



