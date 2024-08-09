import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.WARN, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('This is debus message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('this is an error message')
logging.critical('This is a critical message')


def method1():
    logging.info('This is an beginning of the method')
    print(5 + 6)
    logging.info('This is an End of the method')


method1()
