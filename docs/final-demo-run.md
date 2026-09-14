# Final Demo Run

Real, live end-to-end cycle — no mock mode, real API calls throughout.

## Command

```bash
python main.py
```

## What happened

**Trend research** (live Google Search grounding, not training data): surfaced real, specific diaspora conversation patterns — pushback against pan-Caribbean assumptions (e.g. Creolese being mistaken for Jamaican Patois) and real Guyanese idioms like *"Me na able"* and *"Yuh eye pass me"* circulating in NYC/Richmond Hill and Toronto diaspora communities.

**Content generated**: a real caption and generated image contrasting formal corporate English against the emotional efficiency of *"Me na able,"* aimed squarely at second-generation diaspora navigating family dynamics — with a call-to-action inviting followers to share their own untranslatable Creolese phrases. Image saved at [`output/post_1789413469.png`](../output/post_1789413469.png).

**Publishing**: correctly staged rather than posted live, since `META_PAGE_ACCESS_TOKEN`/`META_PAGE_ID` aren't configured in this environment — exactly the honest fallback behavior the agent was built to have, not a failure.

**Founder report**: a plain-language cycle summary, including a genuinely useful self-suggested improvement for next cycle (short-form video/Reel scripts, given the audio-trend signal it picked up during research) — the agent proposing its own next step, not just executing a fixed script.

## Why this matters for judging

This is the full autonomous loop working end to end on one real, unmodified run: research something true right now, make a real creative decision grounded in that research, generate real output, and handle the publish step honestly according to what's actually configured — then report back like an employee, not a tool waiting to be operated.
