import os
import click
from app import app

@app.cli.command('test1')
def test1():
    """testing our cli"""
    print("hello world")


@app.cli.group()
def translate():
    """Translation Commands"""
    pass

@translate.command()
@click.argument('lang')
def init(lang):
    """Initalize a new language """
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError("extract command failed")
    if os.system('pybabel init -i messages.pot -d app/translations -l ' + lang):
        raise RuntimeError("init command failed")
    os.remove("messages.pot")


@translate.command()
def update():
    """Update all langugages"""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError("extract command failed")
    if os.system('pybabel update -i messages.pot -d app/translations'):
        raise RuntimeError('update command failed')
    os.remove("messages.pot")

@translate.command()
def compile():
    """Compile all languages"""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile command failed')