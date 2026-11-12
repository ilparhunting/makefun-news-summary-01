#!/usr/bin/env python3
"""make.fun bounty entry: news-summary-01.

Writes a summary of the world's news of Wednesday 11 November 2026
to /output/entry.txt.

The summary is embedded in this file, so the program is fully
deterministic and needs no network: every run writes exactly the
same bytes. If /output does not exist (local testing), it writes to
output/entry.txt next to this file instead.
"""

from pathlib import Path

SUMMARY = '''Wednesday 11 November 2026

The war with Iran wound down: on Monday, President Trump called it "militarily effectively over", and on Tuesday Secretary of State Marco Rubio said economic pressure had worked so well there was "really no need for major combat operations". But the Strait of Hormuz stayed shut for over 250 days, and Iran's negotiator said it would "never return" to its pre-war state.

In Abu Dhabi, Russia and Ukraine agreed their largest prisoner exchange of the war — more than 1,000 on each side, in two to three weeks — but no ceasefire, after the first trilateral talks in nine months. US envoys Jared Kushner and Steve Witkoff head to Moscow on Thursday to see Vladimir Putin.

In Gaza, Israeli strikes killed three people on Wednesday, including two brothers sheltering in a tent, and floods swamped about 70,000 tents sheltering displaced families, with a million people at flood risk.

In Sudan, UNICEF said drones caused two in three child casualties this year, as strikes on power stations left the grid near collapse.

At COP31 in Turkey, UN chief Antonio Guterres warned the world was on "a path to destruction" unless climate action speeds up.

Spain held its first general strike in 14 years: unions said four million workers stopped over housing costs, and marches in Madrid and Barcelona turned violent in the evening.

China's trade surplus passed $1 trillion in the first ten months — $1.04 trillion, a record pace.

Anthropic, the maker of Claude, launched its IPO roadshow, offering 825 million shares at $70-$78 for up to a $1.4 trillion valuation.

In the US, hot inflation — consumer prices up 0.4% in October — raised December Fed hike bets, the House shelved impeaching defence secretary Pete Hegseth, and a 41-year-old US soldier was arrested in Britain on suspicion of spying for Russia.

And Elliptic said about $3.1 billion of the $6.3 billion stolen from Binance in October was still in the thieves' wallets, days after its finance chief stepped down.
'''

TARGETS = (
    Path("/output/entry.txt"),
    Path(__file__).resolve().parent / "output" / "entry.txt",
)


def main() -> None:
    for target in TARGETS:
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(SUMMARY, encoding="utf-8")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt")


if __name__ == "__main__":
    main()
