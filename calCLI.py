from mylib.calc import add, sub, mul, div, power
import click

@click.group()
def cli():
    """
    A calculator program
    """
@cli.command("add")
@click.argument('a',type=float)    
@click.argument('b',type=float)  
def add_cmd(a,b):
    """Add two numbers
    Example:
    ./calCLI.py add 1 2
    """ 
    click.echo(f"{a} + {b} ={add{a,b}}",fg="green")

def add_cmd(a,b):
    """Add two numbers
    Example:
    ./calCLI.py add 1 2
    """ 
    click.echo(f"{a} - {b} ={sub{a,b}}",fg="green")    