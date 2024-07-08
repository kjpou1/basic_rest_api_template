import logging

from flask import Blueprint, jsonify, request

from app.config.config import Config

api_bp = Blueprint("api", __name__)
logger = logging.getLogger(__name__)


@api_bp.route("/api/salutatio", methods=["GET"])
def greet_user():
    """
    Serve a greeting message.

    Returns:
    JSON response with a greeting message.
    """
    name_param = request.args.get("name", "anonymous")
    salutation = f"Salve: {name_param}"
    data = {"greeting": salutation}
    return jsonify(data), 200


def print_all_endpoints(app, config=Config()):
    """
    Print all registered URL endpoints.

    Parameters:
    app (Flask): The Flask application instance.
    config (Config): The configuration instance.
    """
    host = config.server_host
    port = config.server_port
    box_width = 50
    logger.info("%s", "┌" + "─" * (box_width - 2) + "┐")
    logger.info(
        "%s",
        "│"
        + "\033[95m"
        + " Registered URL Endpoints:".center(box_width - 2)
        + "\033[0m"
        + "│",
    )
    logger.info("%s", "├" + "─" * (box_width - 2) + "┤")
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            url = f"http://{host}:{port}{rule}"
            endpoint_str = f"{rule.endpoint}: {url}"
            logger.info(
                "%s",
                "│" + "\033[94m" + endpoint_str.ljust(box_width - 2) + "\033[0m" + "│",
            )
    logger.info("%s", "└" + "─" * (box_width - 2) + "┘\n")
