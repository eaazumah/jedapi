#!/usr/bin/env bash
source env/bin/activate
export MODE=PRODUCTION
#export DATABASE_URL="[DIALECT]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DATABASE]"
#GUNICORN_CMD_ARGS="--bind=0.0.0.0 --worker-class eventlet -w 1 --log-level=debug --reload" gunicorn main:app
#GUNICORN_CMD_ARGS="--bind=0.0.0.0 --log-level=debug --reload --timeout=90" gunicorn main:app
