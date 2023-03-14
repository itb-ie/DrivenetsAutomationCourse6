import logging
import colorlog

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# I need to create the color log object to set the color parameters
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create the color formatter
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s -- %(asctime)s -> %(message)s',
    datefmt='%A %H:%M:%S',
    log_colors={
        'DEBUG': 'yellow', 'INFO': 'light_green', 'WARNING': 'bold_purple', 'ERROR': 'cyan', 'CRITICAL': 'bold_red'}
)

# add the formatter to the ch
ch.setFormatter(formatter)

# last step: add the ch to the logger
logger.addHandler(ch)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.info("This is an info message")
logger.error("This is an error message")
logger.critical("This is a critical message")
logger.info("This is an info message")
