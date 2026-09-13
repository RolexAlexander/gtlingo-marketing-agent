# Devpost Submission Pitch — Agents for Humans Hackathon

**Track:** Professional Agents

## Problem

Small business owners and solo founders know they should be marketing consistently on social media, but it competes with every other job they're already doing themselves. The result is a common, specific failure mode: marketing happens in bursts (a founder blocks off a Saturday to "catch up on Instagram") rather than continuously, and even then, decisions about *what* to post are usually gut-feel rather than grounded in what's actually resonating right now. This isn't a tooling gap — scheduling and design tools already exist — it's a continuous-attention gap. Nobody's job is to notice a trend on Tuesday and have a post ready by Wednesday.

## Audience

Solo founders and small teams running a real product or local business who have no dedicated marketing hire — the exact audience this hackathon's "Professional Agents" track targets. Demoed against [GTLingo](https://github.com/RolexAlexander/GTLingo), a real Guyanese Creolese translation app, but the brand profile is swappable (`marketing_agent/brand_profile.py`) — this isn't logic hard-coded to one business.

## What it does, and why it's an agent and not an app

This doesn't ask the founder to log in and check a dashboard. It runs a full cycle on its own: research real, current trends relevant to the brand (via live Google Search grounding, not stale training data), generate a real post — caption and image — in the brand's authentic voice grounded in that research, publish it (a real Facebook post via direct Graph API upload) or stage it honestly for approval when live publishing isn't configured, and report back in plain language, like an employee giving a status update, not a tool waiting to be operated. The founder's only job is to read the one-paragraph summary at the end.

## Impact

The measurable claim is narrow and honest: this replaces the *decision and production* labor of one marketing cycle (what to post, writing it, making the image, publishing it) with a single review step. It does not claim to replace strategy or brand judgment — the founder still sees every post before it counts as "done" whenever live publishing isn't wired up, and even when it is, the brand profile and content pillars are still human-authored constraints the agent works within, not decisions it makes unsupervised.

## Honest scope note

Instagram publishing is staged, not live, in this submission — its Content Publishing API requires a public image URL this build doesn't host yet, documented plainly in the README rather than worked around with a shortcut. Facebook publishing is genuinely live. This is a deliberate choice to submit something real and verifiable over something that looks more complete but isn't accurately described.
