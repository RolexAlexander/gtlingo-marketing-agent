import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
META_PAGE_ACCESS_TOKEN = os.environ.get("META_PAGE_ACCESS_TOKEN", "")
META_IG_USER_ID = os.environ.get("META_IG_USER_ID", "")
META_PAGE_ID = os.environ.get("META_PAGE_ID", "")
MOCK = os.environ.get("MARKETING_MOCK", "0") == "1"

TEXT_MODEL = "gemini-flash-latest"
IMAGE_MODEL = "gemini-2.5-flash-image"

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
STAGED_DIR = OUTPUT_DIR / "staged_posts"
STAGED_DIR.mkdir(parents=True, exist_ok=True)
