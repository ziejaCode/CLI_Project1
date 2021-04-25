import click

@click.command()
@click.option('--firstname','-f',help="First name", type=str, default="Friend")
@click.option('--num','-n',help="number", type=int, default=1)
@click.option('--salary','-s',nargs=2)
@click.option('--city','-c', help="Your cities", multiple=True)
@click.version_option('0.01',prog_name='basic_cli')
def main(firstname, num, salary, city):
    """ A Simple CLI """
    click.echo("Hello CLI {} and you are {} on the queue".format(firstname, num))
    print(city)

if __name__ == '__main__':
    main()
