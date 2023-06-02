# coding: utf-8
"""Module for files IO utilities."""
import gzip
import logging
from json import dumps, loads
from pathlib import Path
from typing import Any, Dict, Iterable, List, Union


def write_dict_list_to_jsonl_gz(filepath: Path, container: List[Dict]):
    """Write a list of dict to jsonl.gz."""
    logging.info("Writing data to %s", filepath)
    with gzip.open(filepath, "w") as fo:
        for entry in container:
            fo.write("{}\n".format(dumps(entry, separators=(",", ":"))).encode("utf-8"))


def read_dict_list_from_jsonl_gz(filepath: Path) -> Iterable[Dict[str, Any]]:
    """Read jsonl.gz file and yield dict."""
    logging.info("Reading data from %s", filepath)
    with gzip.open(filepath, "r") as lines:
        for line in lines:
            data = loads(line)

            yield data


def mkdir(path: Union[str, Path]) -> Path:
    """Given a path, create the directories tree.

    Return a Path object
    """
    path = Path(path)

    if path.suffix:
        dir_path = path.parent
    else:
        dir_path = path

    if not path.exists():
        logging.info("Path %s does not exists, it will be created", dir_path)

    dir_path.mkdir(parents=True, exist_ok=True)

    return path
