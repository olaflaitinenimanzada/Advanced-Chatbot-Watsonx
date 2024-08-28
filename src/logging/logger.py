import logging
import os
from config import LOGS_PATH

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

assistant_logger = setup_logger('assistant_logger', os.path.join(LOGS_PATH, 'assistant.log'))
nlu_logger = setup_logger('nlu_logger', os.path.join(LOGS_PATH, 'nlu.log'))
tone_analyzer_logger = setup_logger('tone_analyzer_logger', os.path.join(LOGS_PATH, 'tone_analyzer.log'))
discovery_logger = setup_logger('discovery_logger', os.path.join(LOGS_PATH, 'discovery.log'))
web_logger = setup_logger('web_logger', os.path.join(LOGS_PATH, 'web.log'))
