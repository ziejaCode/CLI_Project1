import click

# @click.command()
# @click.argument('file_name', required=True)
# def download(file_name):
#     """ Download file """
#     click.confirm("Do you want to continue downloadin ", abort=True, default=True)
#     click.echo("Downloading {}".format(file_name))


@click.command()
@click.argument('file_name', required=True)
@click.confirmation_option(prompt='Do you want to continue downloadin')
def download(file_name):
    """ Download file """
    click.echo("Downloading {}".format(file_name))


if __name__=='__main__':
    download()