# web-security-checker
Term project for Software Engineering 2019


### Hello World


### Install need package
``
pip install -r requirements.txt
``

### Run server (src/WebApplication)
python manage.py runserver 

### Run unit tests
``
python -m unittest discover ./tests/
``

This command will run all "**test\***" in tests/
Be careful that all test files should be modules or packages (including namespace packages) importable from the top-level directory of the project (this means that their filenames must be valid identifiers).
That means one need to add "\_\_init\_\_.py" in order to use this command to run your test file.

``
python -m unittest tests/SourceCodeHandlerTest/SourceCodeHandlerTest.py
``

This command can run the specific test file you want.





