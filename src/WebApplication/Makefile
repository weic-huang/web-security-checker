python=python3
pip=pip3

unittest:
# 	$(python) manage.py test tests/BrowserSimulatorTest/
# 	$(python) manage.py test tests/SourceCodeHandlerTest/
	$(python) manage.py test tests/BlacklistManagerTest/

test:
	$(python) manage.py test tests/CasesTest/

build:
	$(pip) install -r ../../requirements.txt
	$(python) manage.py makemigrations
	$(python) manage.py migrate
	$(python) manage.py loaddata WebApp/fixtures/MininglistDb.json WebApp/fixtures/blacklistDB.json

run:
	$(python) manage.py runserver

clean:
	rm WebApp/static/img/screenshot/*
