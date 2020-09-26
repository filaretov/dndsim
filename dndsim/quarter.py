from __future__ import annotations

from typing import List
from dataclasses import dataclass


@dataclass
class QuarterModel:
    """A quarter contains factions battling over districts."""

    factions: List[FactionAgent]
    districts: List[District]

    def step(self) -> "QuarterModel":
        # logger.debug(f"Pre: {self}")
        new_qm = QuarterModel(
            [faction.step(self.districts) for faction in self.factions], self.districts,
        )
        # logger.debug(f"Post: {new_qm}")
        return new_qm
