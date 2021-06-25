import sys
from getopt import getopt, GetoptError
import logging
from logging import Logger
from pythonjsonlogger import jsonlogger

SHELL_MODE = False
FILTER_FILE = 'input_file.ext'
SOURCE_TEXT = 'other_file.ext'

def init_logger() -> Logger: 
    # Set a useful log format
    log_format = '%(asctime)s %(levelname)s %(thread)d %(name)s %(message)s %(filename)s %(funcName)s %(lineno)d %(pathname)s %(process)d'

    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    # Create console handler and set level to debug
    console_handler = logging.StreamHandler()

    formatter = jsonlogger.JsonFormatter(log_format)
    # Add formatter to console_handler
    console_handler.setFormatter(formatter)

    # Add console_handler to logger
    logger.addHandler(console_handler)

    return logger


# Setup global logger
LOGGER = init_logger()

def validate_input(args: list[str]):
    '''Example validations on the input. Checks:
    - Two values
    - Each must end in .txt

    Args:
        args (list[str]): Input from the command line
    '''
    # Check for correct number of arguments
    if len(args) != 2:
        LOGGER.error(f'Error: Called with {len(args)} arguments. Must be 2. Usage: [poetry run python app.py -s] or [make run] example_input_file.ext example_other_file.ext')
        sys.exit(1)

def parse_file(file_path: str) -> str:
    '''Open, read and potentially parse a file in this method

    Args:
        file_path (str): Path to file

    Returns:
        str: Contents of file
    '''
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def main(argv: list[str]) -> None:
    '''Main. Reads in from command line, outputs.

    Args:
        argv (list[str]): Command line arguments
    '''

    # Create logger that is just for printing the output with nothing else
    print_logger = logging.getLogger('print_logger')
    print_logger.setLevel(logging.INFO)

    # Create console handler and set level to debug
    print_handler = logging.StreamHandler()

    # Add print_handler to logger
    print_logger.addHandler(print_handler)

    # Get command line arguments
    try:
        opts, args = getopt(argv, 'ds')
    except GetoptError:
        LOGGER.error('Error: Program called wrong from command line. Usage: [poetry run python app.py -s] or [make run] example_input.ext example_other.ext', extra={'argv':argv})
        sys.exit(1)

    # Parse command line arguments and options
    for option, argument in opts:
        if option == '-h':
            # Help/how to run
            print_logger.info(Usage: [poetry run python app.py -s] or [make run] example_input.ext example_other.ext'Usage: [poetry run python app.py -s] or [make run] (-d) example_input.ext example_other.ext')
            sys.exit()
        if option == '-d':
            # Run in debug mode 👾
            LOGGER.setLevel(logging.DEBUG)
            LOGGER.debug('Running in debug mode')
            LOGGER.debug(f'Argv: {argv}')
            LOGGER.debug(f'Command line options: {opts}')
            LOGGER.debug(f'Command line arguments: {args}')
        if option == '-s':
            # Running in shell mode
            LOGGER.debug('Running in shell mode')
            # Had to refence global because the assignment here was making python create a local var
            #   instead of using the global one, why? 🤷
            global SHELL_MODE 
            SHELL_MODE = True

            # Make sure input is valid for shell mode
            validate_input(args)

    # Parse the input files
    input_file_contents = parse_file((args[0] if SHELL_MODE else FILTER_FILE))
    LOGGER.debug(f'Input file contents: {input_file_contents}')

    print_logger.info('count: 42')

    LOGGER.debug("Program done. Exiting")



if __name__ == "__main__":
    # Grab command line arguments, don't include the program name that is in the [0] position
    main(sys.argv[1:])