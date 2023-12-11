import logging
import os
from logging.handlers import RotatingFileHandler


class LoggerManager:
    def __init__(self, log_file='logs/app.log', log_level=logging.DEBUG):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if not os.path.exists(log_file):
            open(log_file, 'w').close()

        file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024 * 100, backupCount=20)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def info(self, message: any):
        self.logger.info(message)

    def debug(self, message: any):
        self.logger.debug(message)

    def warning(self, message: any):
        self.logger.warning(message)

    def error(self, message: any):
        self.logger.error(message)
