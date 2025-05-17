# better-docker-voting-app

*!!this project is created by docker.io, i have fixed some aspects of the code since its not maintained anymore!!*
---
**A distributed voting application with real-time results, built with:**

- Frontend: Python/Flask
- Worker: .NET Core
- Results: Node.js/Express
- Data: Redis + PostgreSQL

---

### this is a voting application using 5 microservice 
1. Vote: A frontend application where users can vote for their preferred option.
2. Postgres: A relation database to store only the latest single vote from any device 
3. Redis: An in-memory data store used to temporarily store votes.
4. Worker: A backend service that processes votes stored in Redis and moves them to a PostgreSQL database.
5. Result: A frontend application that displays the real-time voting results.

```bash
┌─────────────┐   ┌────────┐   ┌─────────────┐   ┌─────────────┐
│  Vote       │   │ Redis  │   │ PostgreSQL  │   │ Results     │
│ (Flask)     │──▶│ (Queue)│──▶│ (Database)  │◀──│ (Node.js)│
└─────────────┘   └────────┘   └─────────────┘   └─────────────┘
     ▲                                   ▲
     │                                   │
     └───────────────────────────────────┘
          (.NET Worker processing)
```


# FAKE VOTE
- it will generate fake vote requests.
- in the `fake-vote` directory, just run the shell script and it will generate votes
- to change the number off votes, edit the line `ab -n 100 -c 50 -p posta -T "application/x-www-form-urlencoded" http://localhost:8080/` where `-n` defines the number of votes 
- requires apache package with utils to run ab (apache-benchmark)

# HOW TO RUN
- `git clone https://github.com/luffyxxsenpai/better-docker-voting-app.git`
- `cd better-docker-voting-app`
- `docker compose up --build`

- if succesfull it will be showing something like this
```bash
vote-result    | App running on port 8081
vote-result    | Connected to db
vote-worker    | Connected to db
vote-worker    | Found Redis at 127.0.0.1
vote-worker    | Connecting to Redis
vote-worker    | Worker successfully connected to Redis
```
- `http://localhost:8080` voting interface
- `http://localhost:8081` voting results

- generate some unique votes
- `cd fake-vote && ./generate-votes.sh posta`

- *refer to my dockerhub repo for env requirements*
- `https://hub.docker.com/repositories/luffyxxsenpai/voting-result` 
- `https://hub.docker.com/repositories/luffyxxsenpai/voting-vote` 
- `https://hub.docker.com/repositories/luffyxxsenpai/voting-worker`

# DIR STRUCTURE
```
$ tree -L 2 .
.
├── compose.yaml
├── fake-vote
│   ├── generate-votes.sh
│   ├── make-data.py
│   ├── posta
│   └── postb
├── README.md
├── result
│   ├── Dockerfile
│   ├── node_modules
│   ├── package.json
│   ├── server.js
│   ├── tests
│   ├── views
│   └── yarn.lock
├── vote
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── static
│   └── templates
└── worker
    ├── Dockerfile
    ├── Program.cs
    └── Worker.csproj

```

---