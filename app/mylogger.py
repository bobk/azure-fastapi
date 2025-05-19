from fastapi import logger
import logging
import sys

LOGLEVEL = logging.DEBUG
logger.logger.setLevel(LOGLEVEL)
logger.logger.addHandler(logging.StreamHandler(sys.stdout))

def mylog(text: str):
    """
    d
    """
#    logger.logger.log(level=LOGLEVEL, msg="f")
    logger.logger.log(LOGLEVEL, msg=text)
