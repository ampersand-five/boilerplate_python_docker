import logging

# Set a useful log format
LOG_FORMAT = '%(asctime)s %(levelname)s %(thread)d %(name)s %(message)s %(filename)s %(funcName)s %(lineno)d %(pathname)s %(process)d'

# Configure the logger
logging.basicConfig(
    # filename='output.log', skip in docker container
    encoding='utf-8', 
    level=logging.DEBUG,
    format=LOG_FORMAT)

# Get root logger reference
LOGGER = logging.getLogger(__name__)


LOGGER.debug('test')


main() -> None:
    print('hey')
    LOGGER.info('hey from info logger')

if __name__ == "__main__":
    main()