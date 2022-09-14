import afmvn.query
import logging

def init():
    logging.basicConfig(level=logging.DEBUG)


init()

result = afmvn.query.search("kotlin")
logging.info('result = ' + result)
