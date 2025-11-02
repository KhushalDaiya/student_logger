import logging
import logging.handlers
import os
from typing import Optional

DEFAULT_LOG_FILE = "app.log"

def get_logger(name: str = "student_logger",
               log_file: Optional[str] = None,
               level: int = logging.INFO) -> logging.Logger:
    """
    Return a configured logger that logs to both console and a file.
    - name: logger name
    - log_file: path to file (defaults to ./app.log)
    - level: logging level threshold
    """
    if log_file is None:
        log_file = os.environ.get("STUDENT_LOGGER_FILE", DEFAULT_LOG_FILE)

    logger = logging.getLogger(name)

    if logger.handlers:
        logger.setLevel(level)
        return logger

    logger.setLevel(level)
    logger.propagate = False

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s",
                                  datefmt="%Y-%m-%d %H:%M:%S")

    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    fh = logging.handlers.RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8")
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
