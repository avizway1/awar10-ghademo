# Python Flask App (GitHub Actions demo)

A small Flask web app served by Gunicorn, used to practice CI/CD with GitHub Actions.

## Endpoints

| Path        | Description                          |
|-------------|--------------------------------------|
| `/`         | Web page showing version, env, commit |
| `/health`   | Health check (`{"status": "ok"}`)    |
| `/api/info` | Build/runtime info as JSON           |

## Run locally

```bash
cd python-app
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# dev server (auto-reload)
python app.py                      # http://localhost:5000

# production-style with gunicorn
gunicorn -c gunicorn.conf.py app:app   # http://localhost:8000

# tests
pytest -v
```

## Environment variables

| Variable           | Default | Purpose                                 |
|--------------------|---------|-----------------------------------------|
| `APP_ENV`          | `dev`   | Shown as a badge (dev / uat / prd)      |
| `APP_VERSION`      | `1.0.0` | Shown on the page                       |
| `GIT_SHA`          | `local` | Set to `${{ github.sha }}` in workflows |
| `PORT`             | `8000`  | Gunicorn bind port                      |
| `GUNICORN_WORKERS` | CPU×2+1 | Number of Gunicorn workers              |
