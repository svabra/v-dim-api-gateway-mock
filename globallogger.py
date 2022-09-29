import logging, queue
from pathlib import Path
import logging.handlers
from pytz import timezone
from datetime import datetime

def setup_custom_logger(name):    
    formatter = logging.Formatter('%(asctime)s [%(module)s.%(funcName)s:%(lineno)d] %(levelname)s %(message)s')
    formatter.converter = lambda *args: datetime.now(tz=timezone('CET')).timetuple()

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    log_queue     = queue.Queue()
    queue_handler = logging.handlers.QueueHandler(log_queue)       
    #set the non-blocking handler first
    logger.addHandler(queue_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    
    file = Path(__file__).parent.absolute().joinpath('app_rolling.log')
    timerotating_handler = logging.handlers.TimedRotatingFileHandler(file, when='D', backupCount=30)
    timerotating_handler.setLevel(logging.DEBUG)
    timerotating_handler.setFormatter(formatter)

    
    listener = logging.handlers.QueueListener(log_queue, stream_handler, timerotating_handler, respect_handler_level=True)
        
    listener.start()

    return logger