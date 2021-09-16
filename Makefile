SHELL := /bin/bash

manage_py := python app/manage.py

runserver:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

worker:
	cd app && celery -A settings worker -l info

beat:
	cd app && celery -A settings beat -l info

shell_plus:
	$(manage_py) shell_plus --print-sql