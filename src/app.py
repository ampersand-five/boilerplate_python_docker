import sys
from getopt import getopt, GetoptError
import logging
from logging import Logger
from pythonjsonlogger import jsonlogger


def init_logger() -> Logger: 
    # set a useful log format
    log_format = '%(asctime)s %(levelname)s %(thread)d %(name)s %(message)s %(filename)s %(funcName)s %(lineno)d %(pathname)s %(process)d'

    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    # create console handler and set level to debug
    console_handler = logging.StreamHandler()

    formatter = jsonlogger.JsonFormatter(log_format)
    # add formatter to console_handler
    console_handler.setFormatter(formatter)

    # add console_handler to logger
    logger.addHandler(console_handler)

    return logger

# Setup global logger
LOGGER = init_logger()

def main(argv: list[str]) -> None:
    '''Main. Reads in from command line, outputs.

    Args:
        argv (list[str]): Command line arguments
    '''

    # create logger that is just for printing the output with nothing else
    print_logger = logging.getLogger('print_logger')
    print_logger.setLevel(logging.INFO)

    # create console handler and set level to debug
    print_handler = logging.StreamHandler()

    # add print_handler to logger
    print_logger.addHandler(print_handler)

    # init file vars
    input_file = ''
    output_file = ''

    # get command line arguments
    try:
        opts, args = getopt(argv, 'd')
    except GetoptError:
        LOGGER.error('Error: Program called wrong from command line. Usage: python app.py input.txt output.txt')
        sys.exit(1)

    # parse command line arguments and options
    for option, argument in opts:
        if option == '-h':
            # help/how to run
            print_logger.info('python app.py (-d) input.txt output.txt')
            sys.exit()
        if option == '-d':
            # run in debug mode
            LOGGER.setLevel(logging.DEBUG)
            LOGGER.debug('Running in debug mode')
            LOGGER.debug(f'Argv: {argv}')
            LOGGER.debug(f'Command line options: {opts}')
            LOGGER.debug(f'Command line arguments: {args}')



    print_logger.info('count: 42')



    LOGGER.debug("Program done. Exiting")



if __name__ == "__main__":
    # Grab command line arguments, don't include the program name that is in the [0] position
    main(sys.argv[1:])