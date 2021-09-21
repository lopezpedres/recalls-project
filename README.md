# ems-project

## Environment setup

The `docker-compose.yml` has two services defined:
- The `database` has a single environment configured at `config/database.env`.
- The `app` service has two environments configured at `config/app.env` and `config/app.env.local`.
Here, "local" means when you want to run the flask app directly from the command line, without using docker.

In order to generate the `SECRET_KEY` environment variable for `config/app.env` and `config/app.local.env`, you must generate a random hexadecimal string with 100 characters.

```bash
openssl rand -hex 100
```

For a database password, set the `POSTGRES_PASSWORD` in `config/database.env` by using a random string with 15 characters.

```bash
openssl rand -base64 15
```

## Running the app
```bash
docker-compose up -d
# or for local development
./scripts/start.sh
```