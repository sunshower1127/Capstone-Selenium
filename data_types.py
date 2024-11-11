from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass
class Article:
    en_title: str
    title: str
    subtitle: str
    author: str
    date: str
    body: str
    body_type: Literal["kr", "en"] = "en"
