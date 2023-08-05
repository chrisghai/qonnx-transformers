import os

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
APP_ROOT = Path(__file__).parent.parent.resolve()
APP_TASK = os.environ.get("APP_TASK") or "translation"
