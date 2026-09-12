"""Publishing: real Facebook Page posting via direct multipart image
upload (Graph API's /{page-id}/photos endpoint accepts a binary file
directly -- no public image hosting required, unlike Instagram's Content
Publishing API which requires a public image_url and is left for the
deepening pass). Falls back to staging locally for founder review/approval
when credentials aren't configured, rather than failing or faking success.
"""

import json
import time

import requests
from strands import tool

from marketing_agent.config import MOCK, META_PAGE_ACCESS_TOKEN, META_PAGE_ID, STAGED_DIR

GRAPH_API_VERSION = "v21.0"


@tool
def publish_or_stage_post(caption: str, image_path: str) -> dict:
    """Publish a finished post to Facebook if credentials are configured;
    otherwise stage it locally for the founder to review and approve
    manually. Never fails silently or fakes a successful publish.

    Args:
        caption: The finished caption text, including hashtags.
        image_path: Local path to the generated image file.

    Returns:
        A dict describing what happened: {"status": "published"|"staged"|
        "error", ...}.
    """
    if MOCK or not (META_PAGE_ACCESS_TOKEN and META_PAGE_ID):
        staged_path = STAGED_DIR / f"post_{int(time.time())}.json"
        staged_path.write_text(
            json.dumps({"caption": caption, "image_path": image_path}, indent=2),
            encoding="utf-8",
        )
        return {
            "status": "staged",
            "reason": "No META_PAGE_ACCESS_TOKEN/META_PAGE_ID configured (or mock mode) -- staged for manual review instead of posting live.",
            "staged_path": str(staged_path),
        }

    try:
        with open(image_path, "rb") as f:
            response = requests.post(
                f"https://graph.facebook.com/{GRAPH_API_VERSION}/{META_PAGE_ID}/photos",
                data={"caption": caption, "access_token": META_PAGE_ACCESS_TOKEN},
                files={"source": f},
                timeout=30,
            )
        response.raise_for_status()
        return {"status": "published", "response": response.json()}
    except Exception as exc:  # noqa: BLE001
        return {"status": "error", "error": str(exc)}
