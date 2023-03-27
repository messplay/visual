# logs/logger.py

import logging
import os
from datetime import datetime
from config.config import LOG_DIRECTORY, LOG_LEVEL

def setup_logger() -> logging.Logger:
    """
    Configura el logger y devuelve la instancia del logger.

    :return: Instancia del logger.
    """
    log_level = getattr(logging, LOG_LEVEL, logging.INFO)

    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY)

    log_filename = os.path.join(LOG_DIRECTORY, f"stock_monitor_{datetime.now().strftime('%Y-%m-%d')}.log")

    logger = logging.getLogger("stock_monitor")
    logger.setLevel(log_level)

    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(log_level)

    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

logger = setup_logger()

if __name__ == "__main__":
    # Ejemplo de uso
    logger.info("Esto es una prueba de registro de información.")
    logger.error("Esto es una prueba de registro de error.")
