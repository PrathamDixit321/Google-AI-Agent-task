import logging
from logging import Logger


def get_logger(name: str = "ai_pgos") -> Logger:
    """Return a configured logger for the project.

    This is intentionally minimal and safe for local development. Applications
    can replace or extend this with structured logging (structlog, elk, etc.).
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch = logging.StreamHandler()
        ch.setFormatter(fmt)
        logger.addHandler(ch)
    return logger
