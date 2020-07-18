import sys
import os
import click
# import base_crawler.extractor as extractor
from base_crawler import extractor

""" Console script for Base Crawler.

Commands:
    base  Run base crawler.

base_crawler: Run Selenium-base extractor.
    Options:
    -a, --actions TEXT  path to repository
    -b, --browser TEXT actions file path. default: base_crawler/conf.py
    -t, --timeout NUMBER amount of seconds the Webdriver will use as it's own timeout before throw an error

"""

TYPE_HELP = "Type 'crawler %s --help' to display cli options."
USERS_DATABASE_URL = str(os.environ.get('USERS_DATABASE_URL'))

@click.group()
def cli():
    pass

@click.command()
@click.option("--actions", '-a', default="base_crawler/conf.py", help="Actions file path.\nDefault: base_crawler/conf.py")
@click.option("--browser", '-b', default="chrome", help="Which browser will be instantiatated by Base Crawler (chrome or firefox).")
@click.option("--timeout", '-t', default="30", help="Amount of seconds the Webdriver will use as it's own timeout before throw an error.")
# @click.option('--is_admin', '-a', is_flag=True, help="Flag to indicate this user is an admin.")
def main(actions, browser, timeout):
    """Console script for base_crawler."""
    try:
        click.echo("base_crawler.cli.main")
        extractor.extract(browser, timeout)
        return 0
    except Exception as e:
        print('Failed to run base crawler. ' + str(e))
        print(TYPE_HELP % ('base'))
        return 1

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
