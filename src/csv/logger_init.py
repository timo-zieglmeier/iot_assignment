import os
import json
import logging.config
import sys

def setup_logging():
    #Setup logging configuration

    dirname = os.path.dirname(sys.modules['__main__'].__file__)
    filename = os.path.join(dirname, 'logging.json')

    if os.path.exists(filename):
        with open(filename, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
        get_logger(__name__).warn("Config '.logging.json' not found. Using standard logging settings...")

def get_logger(module_name):
    return logging.getLogger(module_name)