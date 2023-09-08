from mylib.bot import scrape
import click


@click.command()
@click.option(
    "--name", prompt="Wikipedia page to scrape", help="web page you want to scrape."
)
def cli(name):
    result = scrape(name)
    click.echo(click.style(f"{result}:", bg="white", fg="blue"))


if __name__ == "__main__":
    cli()
