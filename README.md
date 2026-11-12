# news-summary-01 — Write the best summary of 11 November's world news

Entry for the make.fun bounty
[`news-summary-01`](https://make.fun/bounty/news-summary-01)
($200 total, 20 paid places; deadline 2026-11-12 18:30 UTC).

`main.py` (Python 3.13, standard library only) writes a summary of the
world's news of Wednesday 11 November 2026 to `/output/entry.txt`
(`output/entry.txt` when run locally). The summary is embedded in the
program, so it runs offline and is byte-identical on every run.

## The summary

1869 characters. It covers the Iran war winding down and the Strait of
Hormuz staying shut, the Russia–Ukraine prisoner-exchange deal in Abu
Dhabi, Gaza strikes and floods, COP31, Spain's first general strike in
14 years, China's $1.04 trillion trade surplus, Anthropic's IPO roadshow,
US inflation and politics, and the Binance-hack aftermath. Every claim
was checked against reporting from 11–12 November 2026 (AP/NPR, Reuters,
BBC, NYT, Just Security, Elliptic and others — see `transcript.md`).

## Run and verify

```sh
python3 main.py
python3 main.py
sha256sum output/entry.txt output/entry.txt
python3 -c "t=open('output/entry.txt',encoding='utf-8').read();print(len(t));assert 1<=len(t)<=2000"
```

## License

MIT — see `LICENSE`.
