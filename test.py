from sensor.logger import logging
from sensor.exception import SensorException
import sys, os

def test_logger_and_Exception():
    try:
        logging.debug("starting the test_logger and Exception")
        result = 3/0
        print(result)
        logging.debug("stopping the test_logger and exception")
    except Exception as e:
        logging.debug((str(e)))
        raise SensorException(e, sys)

if __name__=="__main__":
    try:
        test_logger_and_Exception()
    except Exception as e:
        print(e)