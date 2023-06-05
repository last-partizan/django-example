export PATH := .venv/bin:$(PATH)

install-deps: clean
	virtualenv .venv
	pip install -r requirements.txt

clean:
	rm -rf .venv

celery-worker:
	celery -A app worker --events -l debug

celery-events:
	celery -A app events

start-redis:
	docker compose up -d

stop-redis:
	docker compose down
