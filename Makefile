.PHONY: tests

PYTHON_ENV = .venv/bin/python

install:
	uv pip install -e '.[dev,s3,azure,hf]'

install-dev:
	uv pip install -e '.[dev]'

install-uv:
	brew install uv

tests:
	pytest -sv tests/

venv:
	uv venv

lint:
	$(PYTHON_ENV) -m ruff check .

format:
	$(PYTHON_ENV) -m ruff format .
