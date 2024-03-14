.PHONY: tests

install:
	uv pip install -e .

install-dev:
	uv pip install -e '.[dev]'

install-uv:
	brew install uv

tests:
	pytest -sv tests/

venv:
	uv venv

lint:
	.venv/bin/python -m ruff check .

format:
	.venv/bin/python -m ruff format .
