import logging.config
from base_lib.logger_setup.misc import load_config

logging_config = load_config(r"config.json")
logging.config.dictConfig(config=logging_config)
app_logger = logging.getLogger("app")
ordinary_logger = logging.getLogger("ord")