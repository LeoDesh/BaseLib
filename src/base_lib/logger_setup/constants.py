import logging.config
from base_lib.logger_setup.misc import load_config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging_config = load_config(BASE_DIR / "config.json")
logging.config.dictConfig(config=logging_config)
app_logger = logging.getLogger("app")
ordinary_logger = logging.getLogger("ord")