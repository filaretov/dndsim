from dataclasses import dataclass, field
from typing import List, Dict

from .resources import Resources


@dataclass
class District:
    name: str
    poi: List[str]
    resources: Resources

    def __contains__(self, item):
        return item in self.poi
