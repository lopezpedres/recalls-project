# export the environment variables
set -a
# relative to current script
source $(dirname "$0")/../config/app.local.env
set +a

# if PYTHON_VENV is set, then activate it
if [ -n "$PYTHON_VENV" ]; then
  source ./venv/scripts/activate
  #flask db init
  flask db migrate -m "added session_token field in user table"
  flask db upgrade
fi
# this command knows the entrypoint is app/entrypoint.py
flask run