# coding: utf-8
"""Display a corpus in jsonl.gz format."""
import gzip
import logging
import logging.config
import os
import sys
from argparse import ArgumentParser
from json import loads
from pathlib import Path
from pprint import pformat
from typing import Any, Dict, Iterable


def pretty_doc(doc: Dict[str, Any], width: int) -> str:
    """Pretty print doc for display."""
    text_width = max(80, width - 10)
    return "{}\n---\n".format(pformat(doc, sort_dicts=False, width=text_width))


def read_dict_list_from_jsonl_gz(filepath: Path) -> Iterable[Dict[str, Any]]:
    """Read jsonl.gz file and yield dict."""
    logging.info("Reading data from %s", filepath)
    with gzip.open(filepath, "r") as lines:
        for line in lines:
            data = loads(line)

            yield data


def main():
    """Entry point."""
    parser = ArgumentParser(
        description="Display corpus",
    )
    parser.add_argument("--debug", help="Trace more informations.", action="store_true")
    parser.add_argument(
        "-n", "--number", help="Number of doc displayed", type=int, default=10
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Input corpus file accept .jsonl.gz files.",
    )

    args = parser.parse_args()

    if args.debug:
        log_level = "DEBUG"
    else:
        log_level = "INFO"

    logging_config = {
        "version": 1,
        "loggers": {
            "": {
                "level": log_level,
                "handlers": [
                    "console",
                ],
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "NOTSET",
                "formatter": "generic",
            }
        },
        "formatters": {
            "generic": {
                "format": "%(asctime)s %(levelname)-5.5s [%(name)s:%(module)s:%(lineno)s][%(threadName)s] %(message)s"  # noqa
            }
        },
    }
    logging.config.dictConfig(logging_config)
    logging.info("Start.")

    # Check config
    #

    # Select reader
    if not args.input.exists():
        logging.error("Input corpus file %s does not exists.", args.input)
        sys.exit(1)

    try:
        terminal_width, _ = os.get_terminal_size()
    except OSError:
        terminal_width = 80

    for n, doc in enumerate(read_dict_list_from_jsonl_gz(args.input)):
        if n + 1 > args.number:
            break
        os.sys.stdout.write(pretty_doc(doc, terminal_width))

    logging.info(f"Done reading {args.number} from {str(args.input)}.")


if __name__ == "__main__":
    main()
