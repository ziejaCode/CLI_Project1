import click


@click.command()
@click.option('--name', '-n')
def main(name):
    """ desc """
    click.echo(click.style("Hello {}".format(name), fg='blue', bg='white', bold='True'))

    click.secho("Your name is {}".format(name),fg='yellow')

    click.echo("Your name is " + click.style(name,fg='yellow'))

if __name__=='__main__':
    main()