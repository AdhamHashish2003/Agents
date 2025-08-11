PY?=python3

.PHONY: venv install install-dev lint test run-dev up down

venv:
	$(PY) -m venv .venv

install: venv
	. .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

install-dev: venv
	. .venv/bin/activate && pip install -U pip && pip install -r requirements-dev.txt

lint:
	. .venv/bin/activate && ruff check .

test:
	. .venv/bin/activate && pytest -q

run-dev:
	. .venv/bin/activate && uvicorn services.api.main:app --reload --host 0.0.0.0 --port 8000

up:
	docker compose up --build -d

down:
	docker compose down -v
