# coding: utf-8
"""Utilities used across POC commands."""
import os
from json import loads
from math import modf
from pathlib import Path
from typing import Any, Dict, Optional, Union

from dateutil import parser, tz
from dateutil.utils import default_tzinfo

# jsonnet loader, some code idea from AllenNLP project


UTC = tz.UTC
PARIS = tz.gettz("Europe/Paris")


def parse_date(date, default_tz=PARIS):
    """Parse a text date with dateutil.

    if no information are given on time-zone use the given one

    Output an aware datetime.
    """
    try:
        parsed_date = default_tzinfo(parser.parse(date), default_tz)
    except (ValueError, TypeError) as error:
        msg = "Unable to parse date %s (%serror)" % (date, error)
        raise ValueError(msg)

    return parsed_date


def pretty_time_delta(seconds: float) -> str:
    """Return a timedelta as string.

    Use timedelta.total_seconds function
    to get seconds.
    """
    frac_seconds, whole_seconds = modf(seconds)
    miliseconds = round(frac_seconds * 1000)
    seconds = int(whole_seconds)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        return "%dd%dh%dm%ds%dms" % (
            days,
            hours,
            minutes,
            seconds,
            miliseconds,
        )
    elif hours > 0:
        return "%dh%dm%ds%dms" % (hours, minutes, seconds, miliseconds)
    elif minutes > 0:
        return "%dm%ds%dms" % (minutes, seconds, miliseconds)
    elif seconds > 0:
        return "%ds%dms" % (seconds, miliseconds)
    else:
        return "%dms" % (miliseconds)
