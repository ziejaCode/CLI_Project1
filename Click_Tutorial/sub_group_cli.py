import click

@click.group()
def main():
    """ """
    pass

@main.group()
def reverse():
    """ """
    pass

@reverse.command()
@click.argument('name')
def reverse_upper():
    """ """
    click.echo(name[::-1].upper())


@reverse.command()
@click.argument('name')
def reverse_lower():
    """ """
    click.echo(name[::-1].lower())

if __name__=='__main__':
    main()