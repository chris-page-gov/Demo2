PYTHON ?= python3

.PHONY: install-dev test test-fast coverage lint typecheck check check-full precommit

install-dev:
	$(PYTHON) -m pip install -e .[dev]

test:
	$(PYTHON) -m pytest

test-fast:
	$(PYTHON) -m pytest

coverage:
	$(PYTHON) -m pytest --cov=eventbrite --cov=main --cov-report=term-missing

lint:
	$(PYTHON) -m ruff check .

typecheck:
	$(PYTHON) -m mypy

check: lint typecheck test

check-full: lint typecheck coverage

precommit:
	$(PYTHON) -m pre_commit run --all-files
