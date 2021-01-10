from dotenv import load_dotenv
from commands import cli, setup_command, list_command, add_command, index_command

load_dotenv()

cli.add_command(setup_command)
cli.add_command(add_command)
cli.add_command(list_command)
cli.add_command(index_command)


if __name__ == '__main__':
    cli()