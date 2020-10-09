from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

import random

class Scheduler(ABC):
    @abstractmethod
    def __call__(self, factions: List[FactionAgent]) -> List[FactionAgent]:
        pass

class RandomScheduler(Scheduler):
    def __init__(self, n_per_turn: int):
        self.n_per_turn = n_per_turn

    def __call__(self, factions: List[FactionAgent]) -> List[FactionAgent]:
        return random.choices(factions, k=self.n_per_turn)
        
