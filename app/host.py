import asyncio
import logging

from flask import Flask
from werkzeug.serving import run_simple

from app.api.routes import api_bp, print_all_endpoints
from app.config.config import Config
from app.models.command_line_args import CommandLineArgs
from app.runtime.command_line import CommandLine


class Host:
    """
    Host class to initialize and run the Flask application with command line arguments and configuration.

    Attributes:
    args (CommandLineArgs): Command line arguments passed to the script.
    config (Config): Configuration object based on command line arguments.
    logger (Logger): Logger instance for logging messages.
    app (Flask): Flask application instance.
    """

    def __init__(self, args: CommandLineArgs):
        """
        Initialize the Host class with command line arguments and configuration.

        Parameters:
        args (CommandLineArgs): Command line arguments passed to the script.
        """
        self.args = args

        self.config = Config()
        self.config.set_server_host(args.server)
        self.config.set_server_port(args.port)

        self.logger = logging.getLogger(__name__)
        self.setup_logging()

        # Initialize Flask app
        self.app = Flask(__name__)

        # Register blueprints
        self.app.register_blueprint(api_bp)

    def setup_logging(self):
        """
        Setup logging configuration.
        """
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

    def run(self):
        """
        Run the asynchronous run_async method.
        """
        return asyncio.run(self.run_async())

    async def run_async(self):
        """
        Asynchronous method to perform the main logic: Start Flask server in a separate thread.
        """
        self.logger.info("Starting host process.")
        print_all_endpoints(self.app, self.config)

        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(
            None,
            lambda: run_simple(
                self.args.server,
                self.args.port,
                self.app,
                use_debugger=self.config.get("DEBUG", False),
            ),
        )
        await future


if __name__ == "__main__":
    args = CommandLine.parse_arguments()
    host = Host(args)
    host.run()
