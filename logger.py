import logging
import json
from datetime import datetime, timezone, timedelta

class JSONFormatter(logging.Formatter):
    def __init__(self, env="prod", version="123"):
        super().__init__()
        self.env = env
        self.version = version

    def format(self, record):
        now = datetime.now().astimezone() # ISO 8601 with microseconds and timezone
        log_record = {
            "time": now.isoformat(), 
            "level": record.levelname,
            "msg": record.getMessage(),
            "env": self.env,
            "version": self.version,
        }
        return json.dumps(log_record, ensure_ascii=False)

logger = logging.getLogger("jsonLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
file_handler.setFormatter(JSONFormatter(env="prod", version="123"))

logger.addHandler(file_handler)

logger.info("starting url-shortener")
logger.warning("low memory warning")
logger.error("something went wrong")