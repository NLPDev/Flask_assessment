# Setup #
1. Setup for a new python project as normal, we recommend using virtualenv and python 2.7
    * For more details, follow: http://timsherratt.org/digital-heritage-handbook/docs/python-pip-virtualenv/
2. Setup a MySQL database
3. Set your python path, eg `export PYTHONPATH=/path/to/my/repo`
4. Add the pip modules: `pip install -r requirements.txt`
5. Copy config/my_development.cnf.sample to config/my_development.cnf and update with your MySQL information
6. Create your MySQL database (use db name found in sample config file)
7. Add to your environment: `FLASK_ENVIRONMENT=development`
8. Import the seed.sql file into the database
9. Migrate to the latest version of the database with `alembic upgrade head`.
10. Create testing environment: create config/my_test.cnf, setup a test db (using naming convention of development db but that clearly indicates this is your test db), import seed.sql, update new db:`FLASK_ENVIRONMENT=test alembic upgrade head`

### Checkpoint ###
1. Before proceeding further, ensure that you can:
    * see 3 rows in the user table in your database
    * Start the app with `python app_test.py`
    * The page at /dashboard is now visible and welcomes you to the task. This page will automatically log you in as user 1.
    * You can run unit tests with `py.test tests` and see 2 tests passing.


## Assessment Criteria ##
1. Ability to handle ambiguous requirements.
2. Python ability
3. MySQL
4. CSS and Javascript
5. Tests 
6. Development practices / code organization / development tools (eg git)
