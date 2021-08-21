import click

"""This module will show how to open url or file with your cli tool

How to use it:

    python3 launch_cli.py open-url "http://wp.pl"

    python3 launch_cli.py open-file test.txt

    python3 launch_cli.py open-file test.txt --locate true

"""

@click.group()
def main():
    """ CLI launcher """
    

@main.command()
@click.argument('url')
def open_url(url):
    """ open url """
    click.echo("Opening Url")
    click.launch(url)


@main.command()
@click.argument('file')
@click.option('--locate','-l',default=False)
def open_file(file, locate):
    """ open url """
    click.echo("Opening file")
    click.launch(file, locate=locate)


if __name__=='__main__':
    main()