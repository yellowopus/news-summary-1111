"""make.fun news-summary-01 entry writer."""

import os
from pathlib import Path

OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"

SUMMARY = (
    "Wednesday's decisive test was whether diplomacy could slow the wars and risks pulling the world apart. In Abu Dhabi, US-brokered Ukraine-Russia talks used a trilateral format: envoys Steve Witkoff, Jared Kushner and Keith Kellogg shuttled between Vladimir Putin's and Volodymyr Zelenskyy's delegations instead of one room. Kyiv's position remained that a ceasefire could not be bought by recognizing occupied Ukrainian territory, and that any settlement required security guarantees and restored sovereignty. The process produced engagement, but not agreement, on land, security or sanctions relief. "
    "Markets whipsawed over AI risk and policy uncertainty. A report said Nvidia's board was prepared to remove CEO Jensen Huang amid an FBI inquiry; the stock fell about 8% after hours from $173.73, sharpening concern that the AI trade's largest pillar could turn unstable. The Nasdaq still gained 1.56% intraday after CoreWeave's results revived demand expectations. Goldman Sachs added a March Federal Reserve rate hike to its outlook, putting tightening risk back into forecasts. "
    "At COP31's leaders segment in Antalya, UN Secretary-General António Guterres warned it was make-or-break time for a climate-justice pact. Most G7 heads stayed away, weakening political pressure for climate finance, adaptation and loss-and-damage support. Spain held its first housing general strike, with rallies and clashes in Barcelona demanding rent controls and affordable homes. "
    "The WHO warned that the Democratic Republic of the Congo's Ebola response urgently needed support, even as UN-backed early-warning systems saved lives from Japan to Rwanda. In Brooklyn, a deadly building collapse raised questions about inspections and enforcement. Russia said its US ambassador, Alexander Darchiev, died at 66, removing a key diplomatic channel at a tense moment."
)


def target_path() -> Path:
    return Path(os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR)) / ENTRY_FILENAME


def write_entry() -> None:
    path = target_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(SUMMARY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
