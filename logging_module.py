import logging

#def main() -> None:

#logging.basicConfig(level= logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%y %H:%M:%S')

#import helper
'''logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')
logging.error('this is a error message')
logging.critical('this is a critical message')'''

#if __name__ == "__main__":
 # main()

logger = logging.getLogger(__name__)

#create handler

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#set level and the format

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning message')
logger.error('this is a error message')
