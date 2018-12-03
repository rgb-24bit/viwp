init:
	pipenv install --dev --skip-lock

flake8:
	pipenv run flake8 --ignore=E501,F401,E128,E402,E731,F821 app

test:
	pipenv run pytest -s --tb=short


# should set or export FLASK_APP=viwp.py

run:
	pipenv run flask run
