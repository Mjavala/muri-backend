import logging
from logging.handlers import TimedRotatingFileHandler


def main_app_logs():
    try:

        logger = logging.getLogger("db")

        if not logger.hasHandlers():
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                filemode="a",
            )
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            file_handler = logging.handlers.TimedRotatingFileHandler(
                "/root/muri/db.log", when="h", backupCount=24
            )
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.INFO)
            logger.addHandler(file_handler)

        return logging.getLogger("db")
    except Exception as e:
        print("LOGGING SETUP EXCEPTION: {}".format(e))
