# Steps to reproduce bug

## 1. Prepare environment

Creates python venv, install deps, and starts docker-compose with redis.
```sh
make install-deps
make start-redis
```

## 2. Open wezterm

In the first tab, run `make celery-worker`.
Open new tab, run `make celery-events`.
Leave second tab active and minimize wezterm window.

## 3. Open another wezterm window.

Try typing, it will be painfully slow.
