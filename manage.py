import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from functions import app

# app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
	manager.run()