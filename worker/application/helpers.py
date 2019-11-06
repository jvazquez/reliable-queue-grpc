from pathlib import Path

import logconfig


def configure_logging_from_json(logging_configuration_file: str) -> None:
    """
    Configure the logging with the provided file
    :param logging_configuration_file:
    :return:
    """

    logging_file = Path(logging_configuration_file).resolve()
    logconfig.from_json(logging_file)
