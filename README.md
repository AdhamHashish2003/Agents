# Boss Stack

Monorepo for Boss's services. Includes sample FastAPI service and tooling for linting,
testing, and containerization.

## Structure

- `apps/`: front-end applications
- `services/`: API and worker services
- `packages/`: shared libraries
- `infra/`: infrastructure definitions
- `tests/`: test suite
- `codex_tasks/`: prompts and tickets

## Local Runbook

### Option A — venv

```bash
make install-dev
make lint
make test
make run-dev
# open http://localhost:8000/health
```

### Option B — Docker

Ensure Docker Desktop is installed; if `docker compose` not found, install Compose v2 or use `docker-compose`.

```bash
make up
curl http://localhost:8000/health
make down
```
