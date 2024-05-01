import logging
import traceback
try:
    x = [1,2,3]
    val = x[3]
except:
    logging.error("The error is %s", traceback.format_exc())   #if we don't know what is the exact error and to trace it
"""except IndexError as e:
    logging.error(e, exc_info=True)"""