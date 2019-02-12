from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
# import pdb; pdb.set_trace()
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()

