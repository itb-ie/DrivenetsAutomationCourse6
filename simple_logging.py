import logging

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s - %(asctime)s - %(message)s',
                    datefmt='%A %H:%M:%S', filename="my_log.txt")

# first I need to get a logger object!
logger = logging.getLogger()

# we write logs via the debug/info/warning/error/critical methods
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.info("This is an info message")
logger.error("This is an error message")
logger.critical("This is a critical message")
logger.info("This is an info message")

