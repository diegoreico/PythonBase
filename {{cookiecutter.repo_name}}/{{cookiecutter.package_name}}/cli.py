import click
import logging

@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):

    logging.basicConfig(level=logging.INFO)

    if ctx is not None:
        click.echo("An action should be specified. Try --help to check the options")


@main.command("hello")
def hello():
    """ Says hello (wave) """

    logging.info("hello")


if __name__ == "__main__":
    # execute only if run as a script
    print("MAIN")
