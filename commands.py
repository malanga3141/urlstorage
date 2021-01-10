from datebase import Database
from os import getenv
import click
from reposities.urls import save, fetch_categories, fetch_urls

@click.group()
def cli():
    pass


@click.command(name='setup')
def setup_command():
    print('Making table in database')
    db = Database(getenv('DB_NAME'))
    db.create_table('''CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)''')


@click.command(name='list')
def list_command():
    print('Category list:')

    for name in fetch_categories():
        print(name[0])


@click.command(name='add')
@click.argument('category')
@click.argument('url')
def add_command(category: str, url: str):
    print('Adding new url addresses')
    save(category, url)


@click.command(name='index')
@click.argument('category')
def index_command(category: str):
    print(f'List link from category {category}')

    for link in fetch_urls(category):
        print(link[2])