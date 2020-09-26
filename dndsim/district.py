from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class District:
    name: str
    poi: List[str]
    resources: Resources
    scouting_capacity: float = 1
    scouting: Dict[FactionAgent, float] = field(default_factory=lambda: {})
    influence_capacity: float = 1
    influence: Dict[FactionAgent, float] = field(default_factory=lambda: {})

    def __contains__(self, item):
        return item in self.poi

    def generate(self, faction: FactionAgent) -> float:
        return self.resources * (self.influence[faction] / self.influence_capacity)
