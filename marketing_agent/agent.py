"""The autonomous marketing agent, wired on Strands.

Today's model backend is Gemini (strands.models.gemini.GeminiModel) so it's
testable immediately with an existing API key. Swapping to
strands.models.bedrock.BedrockModel is a one-line change for the
deepening pass, once AWS/Bedrock access is set up -- see README.
"""

from strands import Agent
from strands.models.gemini import GeminiModel

from marketing_agent.brand_profile import BRAND_PROFILE
from marketing_agent.config import GOOGLE_API_KEY, TEXT_MODEL
from marketing_agent.tools.generate_post import generate_post
from marketing_agent.tools.publish_post import publish_or_stage_post
from marketing_agent.tools.research_trends import research_trends

SYSTEM_PROMPT = f"""You are the autonomous social media manager for a real small business.
You run in the background and handle marketing end to end without being micromanaged --
the founder should only need to step in for real decisions, not routine execution.

{BRAND_PROFILE}

For each cycle:
1. Use research_trends to find out what's actually happening right now relevant to this brand.
2. Use generate_post to create one real post grounded in that research -- pick whichever
   content pillar the research best supports, don't default to the same one every time.
3. Use publish_or_stage_post to publish it (or stage it if live publishing isn't configured).
4. Finish with a short, direct update for the founder: what you found, what you made, what
   happened when you tried to publish it, and one honest note on what would make the next
   cycle better. This update is the only thing the founder should need to read -- write it
   like a competent employee reporting in, not a verbose AI assistant.
"""


def build_agent() -> Agent:
    model = GeminiModel(client_args={"api_key": GOOGLE_API_KEY}, model_id=TEXT_MODEL)
    return Agent(
        model=model,
        tools=[research_trends, generate_post, publish_or_stage_post],
        system_prompt=SYSTEM_PROMPT,
        name="gtlingo-marketing-agent",
    )
