import click

@click.command()
@click.argument("num1")
@click.argument("num2")
# teh
def main(num1, num2):
    click.echo("Working with pos")
    click.echo(num1, num2)

if __name__=='__main__':
    main()