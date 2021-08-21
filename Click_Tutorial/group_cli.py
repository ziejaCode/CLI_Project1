import click

# Parent Command
@click.group()
def main():
    """ Simple CLI with Group """
    pass

# Child Command
@main.command()
@click.argument('text')
def reverse(text):
    """ Reverse a text """
    click.echo(text[::-1])

 
# Child Command   
@main.command()
@click.argument('text')
def capitalize(text):
    """ Capitalize a text """
    click.echo(text.upper())

if __name__=='__main__':
    main()


