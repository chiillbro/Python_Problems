import logging
import time
from logging.handlers import TimedRotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#s for seconds, m for minutes, h for hours, d for days, we can also mention 'midnight', and week days w0 with means monday
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
   logger.info('Hello World!')
   time.sleep(5)