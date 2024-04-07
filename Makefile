APP = restapi

test:
	@flake8 . --exclude .venv

compose: test # Make compose dependable on test
	@docker-compose build
	@docker-compose up