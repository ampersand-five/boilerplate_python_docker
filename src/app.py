import logging
from logging import Logger
from pythonjsonlogger import jsonlogger


def init_logger() -> Logger: 
    # Set a useful log format
    log_format = '%(asctime)s %(levelname)s %(thread)d %(name)s %(message)s %(filename)s %(funcName)s %(lineno)d %(pathname)s %(process)d'

    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = jsonlogger.JsonFormatter(log_format)
    # add formatter to console_handler
    console_handler.setFormatter(formatter)

    # add console_handler to logger
    logger.addHandler(console_handler)

    return logger

LOGGER = init_logger()

LOGGER.debug('test the logger')


def main() -> None:
    LOGGER.info('hey from main')


if __name__ == "__main__":
    main()