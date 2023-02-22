import click
import logging

from mymodule.common.configuration.config import LoggingConfig
from mymodule.hello.controllers.greetings import GreetingsController
from mymodule.analytics.controllers.analytics import AnalyticsController


def configure_logging() -> None:

    config = LoggingConfig()

    rootLogger = logging.getLogger()

    # removes default logging handler
    rootLogger.handlers.clear()
    rootLogger.setLevel(config.LEVEL)
    logFormatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%d-%m-%Y:%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logFormatter)
    rootLogger.addHandler(stream_handler)

    fileHandler = logging.FileHandler("./app.log")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%d-%m-%Y:%H:%M:%S",
    )
    logging.getLogger().setLevel(logging.INFO)


@main.command("say-hello")
@click.argument("name", type=click.STRING, required=True)
def hello(name):
    controller = GreetingsController()
    result = controller.say_hello_to(name)

    print(result)

@main.command("list-clients")
def list_clients():
    controller = AnalyticsController()
    result = controller.list_clients()

    print(result)

if __name__ == "__main__":
    main()
