# web-security-checker
Term project for Software Engineering 2019


### Hello World


### Install need package
``
pip install -r requirements.txt
``

### Build db (src/WebApplication)
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata WebApp/fixtures/MininglistDb.json WebApp/fixtures/blacklistDB.json  
```


### Run server (src/WebApplication)
``
python manage.py runserver 
``

### Run unit tests (src/WebApplication)
```
python manage.py test .\tests\SourceCodeHandlerTest\  
python manage.py test .\tests\BlacklistManagerTest\  
python manage.py test .\tests\BrowserSimulatorTest\  
```






