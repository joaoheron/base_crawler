import os
import click
import psycopg2
import src.extractor as extractor
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

""" Console script for Base Crawler.

Commands:
    base  Run base crawler.

crawler base: Clones repository and inits it.
    Options:
    -a, --actions TEXT  path to repository
    -b, --browser TEXT actions file path. default: src/conf.py
    -t, --timeout NUMBER amount of seconds the Webdriver will use as it's own timeout before throw an error

"""

TYPE_HELP = "Type 'crawler %s --help' to display cli options."
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
    """ Run base crawler """
    with app.app_context():
        try:
            extractor.extract(browser, timeout)
            return True
        except Exception as e:
            print('Failed to run base crawler. ' + str(e))
            print(TYPE_HELP % ('base'))
            return False

if __name__ == "__main__":
    cli()
