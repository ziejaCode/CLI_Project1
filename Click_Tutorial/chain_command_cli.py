import click

"""This module will show how to chain command together 
to create way to run a few command at the same line
and also how to pass content between functions 

How to use it:
    python3 chain_command_cli.py --name Marian reverse capitalize

    python3 chain_command_cli.py --name Marian capitalize reverse 

    python3 chain_command_cli.py --name Marian reverse 

    python3 chain_command_cli.py --name Marian capitalize

"""

# Parent Command
@click.group(chain=True)
@click.option('--name')
@click.pass_context
def main(ctx, name):
    """ Simple CLI with Group """
    ctx.ensure_object(dict)
    ctx.obj['name'] = name 

# Child Command
@main.command()
@click.pass_context
def reverse(ctx):
    """ Reverse a text """
    new_name = ctx.obj['name']
    click.echo("{}".format(new_name[::-1]))

 
# Child Command   
@main.command()
@click.pass_context
def capitalize(ctx):
    """ Capitalize a text """
    click.echo(ctx.obj['name'].upper())

if __name__=='__main__':
    main()

