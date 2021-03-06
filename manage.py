# !/usr/bin/env python

import os
# class for handling a set of commands
from flask_script import Manager
from flask_migrate import (Migrate, MigrateCommand)
from core import (db, create_app, models)


app = create_app('production')
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
    