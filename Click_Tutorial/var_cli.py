import click

"""
hot to use it:
    python3 var_cli.py 'aaa=alex' 'bbb=bobo' 'ccc=hela' folder
"""

@click.command()
@click.argument('source',nargs=-1)# this version accept multiple arguments
@click.argument('source',nargs=2)# this version accept only 2 arguments
@click.argument('destination')
def main(source, destination):
    for f in source:
        click.echo("Moving {} to folder {}".format(f,destination))


if __name__ == '__main__':
    main()