"""Trend research tool, using Gemini's live Google Search grounding --
verified against the installed google-genai SDK's actual type surface
(types.Tool(google_search=types.GoogleSearch())) before writing this.
"""

from google import genai
from google.genai import types
from strands import tool

from marketing_agent.config import GOOGLE_API_KEY, MOCK, TEXT_MODEL


@tool
def research_trends(topic: str) -> str:
    """Research real, current trends and conversation relevant to a topic
    using live web search -- not the model's training data.

    Args:
        topic: What to research, e.g. "Caribbean Creole language content
            trending on Instagram this week" or "Guyanese diaspora identity
            content that performs well on social media."

    Returns:
        A summary of real, current findings grounded in live search results.
    """
    if MOCK or not GOOGLE_API_KEY:
        return (
            "MOCK MODE: no real search performed. Placeholder finding: "
            f"diaspora-identity and language-pride content tends to perform "
            f"well; would have researched '{topic}' live."
        )

    client = genai.Client(api_key=GOOGLE_API_KEY)
    response = client.models.generate_content(
        model=TEXT_MODEL,
        contents=(
            f"Research current, real trends related to: {topic}. "
            "Summarize concrete, specific findings -- not generic advice. "
            "Cite what's actually happening right now."
        ),
        config=types.GenerateContentConfig(tools=[types.Tool(google_search=types.GoogleSearch())]),
    )
    return response.text or "No findings returned."
