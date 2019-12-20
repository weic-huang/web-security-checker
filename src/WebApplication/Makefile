python=python
pip=pip

test:
	$(python) -m unittest discover ./tests/

build:
	$(pip) install -r ../../requirements.txt
	$(python) manage.py makemigrations
	$(python) manage.py migrate
	$(python) manage.py loaddata WebApp/fixtures/MininglistDb.json WebApp/fixtures/blacklistDB.json

run:
	$(python) manage.py runserver

clean:
	rm WebApp/static/img/screenshot/*
