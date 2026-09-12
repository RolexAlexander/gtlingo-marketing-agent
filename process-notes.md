# Process Notes

## Day 1 (2026-09-11) -- light pass

- Brain dump from Rolex: a proactive agent that handles marketing
  autonomously on Facebook/Instagram -- posts, trend analysis, evolving
  strategy, proactive founder updates. Flagged "not sure" on feasibility.
- Flagged one real risk before committing to the idea: live Meta API
  posting typically needs app review / business verification, which can
  take real days-to-weeks. Resolution: build the full autonomous pipeline
  regardless, and make live-vs-staged publishing an honest, graceful
  fallback rather than a blocker.
- Discovered mid-build that this risk splits by platform, not uniformly:
  Facebook's Graph API `/​{page-id}/photos` accepts direct binary upload
  (no public hosting needed) -- genuinely live-postable today with just a
  Page Access Token. Instagram's Content Publishing API requires the image
  to already be at a public URL, which this build doesn't have yet. Built
  accordingly: Facebook can go live today, Instagram stages honestly.
- Chose GTLingo (Rolex's real Guyanese Creolese translation app) as the
  demo business -- swappable via `brand_profile.py`, not hard-coded.
- Installing `strands-agents` in the global Python environment caused
  version conflicts with `google-adk` (opentelemetry/starlette). Verified
  google-adk still imports afterward, but going forward this project uses
  its own isolated `.venv` to avoid further cross-project dependency
  collisions between the three hackathon repos sharing one machine.
- Real integration traps caught before spending anything, same discipline
  as the last two builds:
  - Verified `strands.models.gemini.GeminiModel` exists as a native model
    backend before assuming Bedrock was the only option -- this made
    today's build testable immediately without needing AWS credentials
    (which aren't configured on this machine yet; `aws sts
    get-caller-identity` confirmed no credentials present).
  - Verified `types.Tool(google_search=types.GoogleSearch())` is a real
    field on the installed google-genai SDK before writing the trend-
    research tool around it.
  - Verified the `@tool` decorator from Strands doesn't change how a
    function can be called directly, before writing tests that call tools
    positionally.
- Built: three real tools (research_trends, generate_post,
  publish_or_stage_post) wired into one Strands Agent with a system prompt
  that runs the full cycle autonomously and reports back once, not a
  narrated step-by-step. All non-LLM integration logic covered by mocked,
  zero-cost tests before any real spend.

## Still needed before submission (deadline: 2026-09-14, 5:00pm PDT)

- One real end-to-end cycle once Rolex provides `GOOGLE_API_KEY`.
- A real Facebook Page + Page Access Token to test live publishing (or
  confirm staging-only is the submission's story).
- AWS account + Bedrock model access if the Bedrock upgrade is worth the
  time investment before the deadline -- optional per the hackathon's own
  rules, worth a deliberate yes/no rather than defaulting into it.
- GitHub repo README requirement: architecture diagram (text-only so far,
  add a visual), demo video (max 5 min), AWS Builder ID for the submission
  form.
