import os
import click
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

""" Console script for extendable_base_dash.

Commands:
  create-user  Creates an user.
  delete-db    Deletes the database for user management.
  init-app     Clones repository and inits it.
  init-db      Creates the user database for user management.
  run-app      Run the web application.

ebd init-app: Clones repository and inits it.
    Options:
    -url, --path-url TEXT  URL to repository

ebd init-db: Creates the user database for user management.
    Options: -

ebd delete-db: Deletes the database for user management
    Options:
    -p, --port TEXT       Port to connect with the database that will be deleted.
    -db, --dbname TEXT    Name of the database that will be deleted.
    -user, --dbuser TEXT  User to connect with the database that will be deleted.
    -pw, --password TEXT  Password to connect with the database that will be deleted.

ebd create-user: Creates an user.
    Options:
    --email TEXT     User's email.
    --name TEXT      User's first name.
    --lastname TEXT  User's last name.
    --password TEXT  User's password.
    -a, --is_admin   Flag to indicate this user is an admin.

ebd run-app: Run the web application.
    Options: -
"""

TYPE_HELP = "Type 'ebd %s --help' to display cli options."
USERS_DATABASE_URL = str(os.environ.get('USERS_DATABASE_URL'))

@click.group()
def cli():
    pass

@cli.command()
@click.option("--actions", '-a', default="src/conf.py", help="Actions file path.\nDefault: src/conf.py")
@click.option("--browser", '-b', default="chrome", help="Which browser will be instantiatated by Base Crawler (chrome or firefox).")
@click.option("--timeout", '-t', default="30", help="Amount of seconds the Webdriver will use as it's own timeout before throw an error.")
# @click.option('--is_admin', '-a', is_flag=True, help="Flag to indicate this user is an admin.")
def base(actions, browser, timeout):
    """ Creates an user. """
    app = create_app()

    with app.app_context():
        try:
            user.name = name
            user.surname = lastname

            if is_admin:
                admin = Admin()
                admin.user = user
                db.session.add(admin)
                print("Admin User created.")
            else:
                print("User created.")

            db.session.commit()
            return True
        except Exception as e:
            print('Failed to create user. ' + str(e))
            print(TYPE_HELP % ('create-user'))
            return False

if __name__ == "__main__":
    cli()
