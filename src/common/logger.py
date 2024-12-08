import logging
import sys
from logging import StreamHandler, Formatter


class Logging(Formatter):
    COLORS = {
        logging.DEBUG: "\x1b[38;20m",
        logging.INFO: "\x1b[32;20m",
        logging.WARNING: "\x1b[33;20m",
        logging.ERROR: "\x1b[31;20m",
        logging.CRITICAL: "\x1b[31;1m",
    }
    RESET = "\x1b[0m"

    def format(self, record):
        log_level_color = self.COLORS.get(record.levelno, self.RESET)
        log_fmt = log_level_color + "%(levelname)s" + self.RESET + ":     %(message)s"
        formatter = Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = StreamHandler(sys.stdout)
console_handler.setFormatter(Logging())

logger.addHandler(console_handler)

logger.propagate = False
