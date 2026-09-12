"""GTLingo Marketing Agent -- CLI entrypoint.

Runs one full autonomous marketing cycle: research real trends, generate a
brand-voiced post, publish it (or stage it for approval), and report back.

Usage:
    python main.py
"""

from marketing_agent.agent import build_agent
from marketing_agent.config import GOOGLE_API_KEY, MOCK


def run() -> None:
    if not MOCK and not GOOGLE_API_KEY:
        print("[warning] No GOOGLE_API_KEY set -- tools will fall back to mock output.\n")

    agent = build_agent()
    result = agent("Run today's marketing cycle.")
    print(result)


if __name__ == "__main__":
    run()
