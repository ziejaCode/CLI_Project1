import click

"""This module will show how to add prompt functionality to your cli tool

How to use it:
    python3 prompt_cli.py --firstname Mary

    python3 prompt_cli.py --lastname Roden
    Firstname: Mary

    python3 prompt_cli.py --firstname Mary --lastname Roden

"""

# to comment multipel line Ctrl-k-c
# uncomment Ctrl-k-u

# # this is first method to create prompt
# @click.command()
# @click.option('--firstname','-f', prompt=True)
# @click.option('--lastname','-f')
# def main(firstname, lastname):
#     """ description """
#     click.echo("Your name is {} {}".format(firstname, lastname))


# this is second method to create prompt that lets you customise prompt message
# @click.command()
# @click.option('--firstname','-f', prompt='Enter your first name')
# @click.option('--lastname','-f')
# def main(firstname, lastname):
#     """ description """
#     click.echo("Your name is {} {}".format(firstname, lastname))


# this is third method to create prompt that lets you customise prompt message
# @click.command()
# def main():
#     """ description """
#     fname = click.prompt("Enter you fname")
#     click.echo("Your name is {}".format(fname))


# this is fourth method to create prompt
@click.command()
@click.option('--firstname','-f', prompt=True)
@click.option('--password','-p', prompt=True, hide_input=True, confirmation_prompt=True)
def main(firstname, password):
    """ description """
    click.echo("Your name is {} {}".format(firstname, password))



if __name__=='__main__':
    main()