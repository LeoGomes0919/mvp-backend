import logging
from logging.handlers import RotatingFileHandler


class LoggerManager:
    def __init__(self, app=None):
        self.app = app
        self.init_app()

    def init_app(self):
        if self.app:
            self.configure_logger()

    def configure_logger(self):
        logging.basicConfig(level=logging.INFO)

        handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
        handler.setLevel(logging.INFO)
        self.app.logger.addHandler(handler)

    def log_info(self, message):
        if self.app:
            self.app.logger.info(message)

    def log_error(self, message):
        if self.app:
            self.app.logger.error(message)

    def log_warning(self, message):
        if self.app:
            self.app.logger.warning(message)
