from __future__ import annotations

from dataclasses import dataclass
from typing import List
from loguru import logger


@dataclass
class FactionAgent:
    """A faction spends resources to control districts according to their preferences."""

    resources: Resources
    behaviour: Behaviour
    name: str = ""

    def step(self, districts: List[District]) -> FactionAgent:
        target_district = self.behaviour.pick(districts)
        logger.debug(f"Picked {target_district}")
        new_fa = FactionAgent(
            self.resources + target_district.resources,
            self.behaviour,
            self.name,
        )
        logger.debug(f"New agent: {new_fa}")
        return new_fa

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


# legends say that the infamous "Thugs 4 Less" secretly rule all districts in the Harbour Quarter
