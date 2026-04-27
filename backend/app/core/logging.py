import logging

def setup_logger():
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


logger = setup_logger()