# Sample Dockerized Postgres

Features:

- Volume for persistent data between runs
- PGAdmin out of the box

## Running

Create a new `.env` file based on `.env.example` provided. Then, run `docker-compose up`. You should be able to connect to pgadmin at 0.0.0.0:80. Sign in using your chosen `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`. You will then be able to connect to server by specifying the hostname `database` along with your chosen password for the `postgres` user.

We use a specified volume for pgadmin so that we persist pgadmin data between runs without worrying about stepping on eggshells with our commands.