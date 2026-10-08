#!/usr/bin/env python3
"""Visual/content safety gate for the public GitHub profile README (stdlib only)."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


# Layout baseline is editorial, not an auto-generated repo inventory.
check(len(text) <= 5000, "Keep README <= 5000 characters; move details to PROJECTS.md.")
check(len(re.findall(r"^## ", text, re.MULTILINE)) <= 5, "Limit the profile to five short sections.")
check(not re.search(r"^\s*\|.*\|\s*$", text, re.MULTILINE), "Avoid dense Markdown tables on the profile.")

# Protect key brand/visual assets from an accidental full README rewrite.
for asset in ("assets/context-engineering-banner.svg", "assets/positioning-path.svg"):
    check(asset in text, f"Missing editorial illustration: {asset}")
    check((ROOT / asset).is_file(), f"Local visual asset does not exist: {asset}")

expertise = (
    "Context%20Engineering",
    "Marketing%20Strategy",
    "Knowledge%20Architecture",
    "Agent%20Skills",
    "Responsible%20AI",
)
for label in expertise:
    check(f"img.shields.io/badge/{label}-" in text, f"Missing expertise badge: {label}")

credential_alt = ("Google Cloud", "Databricks", "ESPM")
images = re.findall(r"<img\b[^>]*>", text, re.IGNORECASE)
for label in credential_alt:
    check(any(label in image for image in images), f"Missing verified credential image: {label}")
check(len(images) >= 3, "Keep at least three visual credentials linked to verification.")

social_badges = ("Newsletter-", "Speaking-", "Portfolio-", "LinkedIn-")
for label in social_badges:
    check(f"img.shields.io/badge/{label}" in text, f"Missing social/action badge: {label}")

# Keep traceable evidence and provenance; avoid silent author-credit changes.
for required in (
    "context-engineering-for-marketing",
    "marketing-context-system",
    "cereja",
    "bussola",
    "PROJECTS.md",
    "CREDENTIALS.md",
    "theguitarvity",
):
    check(required.lower() in text.lower(), f"Missing important profile reference: {required}")
check(
    "Victor" in text and ("led" in text or "original" in text),
    "The Bússola project must retain credit for Victor's original technical work.",
)

if errors:
    print("Profile README editorial gate failed:")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)

print("Profile README editorial gate passed (layout, badges, credentials, links, provenance).")
