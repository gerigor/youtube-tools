import logging
import sys
from datetime import datetime


def setup_logging(name: str):
    """Setup displaying logs in terminal and writing them into log files."""

    log_filename = f"logs/{name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter("%(message)s"))
    logging.basicConfig(
        level=logging.INFO, handlers=[logging.FileHandler(log_filename), stream_handler]
    )