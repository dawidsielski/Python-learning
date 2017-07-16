import logging
import time

logging.basicConfig(level=logging.DEBUG, filename="log_file.log")

def print_time():
    logging.debug("Time now is: {}".format(time.time()))






print_time()