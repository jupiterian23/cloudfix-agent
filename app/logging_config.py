"""Logging configuration for CloudFix Agent."""

import logging
from pathlib import Path


def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_dir / "cloudfix.log"),
            logging.StreamHandler(),
        ],
        force=True,
    )

    return logging.getLogger("cloudfix")
