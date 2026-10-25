#!/usr/bin/env python

import argparse
import sys

import requests

API_URL = "https://en.wikipedia.org/w/api.php"

# Wikimedia requires an identifiable User-Agent: tool name/version + contact.
USER_AGENT = "WikipediaPlainText/0.1.2 (https://github.com/rmmonster/wikipedia_article_as_plain_text; git.phil@daxbau.net)"


def fetch_plain_text(title: str, full: bool = False, verbose: bool = False) -> str:
    params = {
        "action": "query",
        "format": "json",
        "formatversion": 2,  # pages becomes a list, not a dict keyed by id
        "titles": title,
        "prop": "extracts",
        "explaintext": 1,
        "redirects": 1,  # follow redirects
    }
    if not full:
        params["exintro"] = 1  # intro section only

    response = requests.get(
        API_URL,
        params=params,
        headers={"User-Agent": USER_AGENT},
        timeout=10,
    )
    if verbose:
        print(f"GET {response.url} -> {response.status_code}", file=sys.stderr)
    response.raise_for_status()

    pages = response.json()["query"]["pages"]
    page = pages[0]
    if page.get("missing"):
        raise LookupError(f"No Wikipedia article found for {title!r}")
    return page.get("extract", "")


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="WikipediaPlainText",
        description="Wikipedia article as plain text",
    )
    parser.add_argument("article_name")
    parser.add_argument(
        "-f",
        "--full",
        action="store_true",
        help="whole article instead of just the intro",
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    try:
        print(fetch_plain_text(args.article_name, args.full, args.verbose))
    except (requests.RequestException, LookupError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
