install:
	uv sync --dev
build:
	uv build
package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check gendiff
test:
	uv run pytest
test-coverage:
	uv run pytest tests/ --cov=gendiff --cov-report=term --cov-report=xml:coverage.xml