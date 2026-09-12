"""Content generation: caption + a real generated image, in the brand's
voice, informed by trend research. Uses the same verified Gemini
generateContent image-generation approach as the Agentic Cinema build
(gemini-2.5-flash-image via generate_content, not the Vertex-only Imagen
generate_images endpoint).
"""

import time

from google import genai
from strands import tool

from marketing_agent.brand_profile import BRAND_PROFILE
from marketing_agent.config import GOOGLE_API_KEY, IMAGE_MODEL, MOCK, OUTPUT_DIR, TEXT_MODEL


@tool
def generate_post(trend_findings: str, content_pillar: str) -> dict:
    """Generate a real social media post -- caption text plus an image --
    in the brand's authentic voice, informed by real trend research.

    Args:
        trend_findings: Real research findings (from research_trends) to
            ground this post in something actually happening, not generic.
        content_pillar: Which content pillar this post should draw from
            (see the brand profile), e.g. "a real Creolese phrase and its
            meaning" or "a diaspora identity moment."

    Returns:
        A dict with "caption" (str) and "image_path" (str, local file).
    """
    if MOCK or not GOOGLE_API_KEY:
        return {
            "caption": f"MOCK MODE placeholder caption for pillar: {content_pillar}",
            "image_path": "",
        }

    client = genai.Client(api_key=GOOGLE_API_KEY)

    caption_prompt = (
        f"{BRAND_PROFILE}\n\n"
        f"Real current trend research to draw from:\n{trend_findings}\n\n"
        f"Write ONE Instagram/Facebook caption for the content pillar: "
        f"'{content_pillar}'. Match the brand voice exactly. Include 3-5 "
        f"relevant hashtags at the end. Output ONLY the caption text."
    )
    caption_resp = client.models.generate_content(model=TEXT_MODEL, contents=caption_prompt)
    caption = (caption_resp.text or "").strip()

    image_prompt = (
        f"A warm, authentic social media image for a Guyanese Creolese "
        f"translation app. Content pillar: {content_pillar}. Caption context: "
        f"{caption}. Style: warm, culturally specific to Guyana/Caribbean, "
        f"NOT a generic stock-photo tropical aesthetic -- real cultural "
        f"texture and specificity."
    )
    image_resp = client.models.generate_content(model=IMAGE_MODEL, contents=image_prompt)

    image_path = ""
    for part in image_resp.candidates[0].content.parts:
        if part.inline_data is not None:
            path = OUTPUT_DIR / f"post_{int(time.time())}.png"
            path.write_bytes(part.inline_data.data)
            image_path = str(path)
            break

    return {"caption": caption, "image_path": image_path}
