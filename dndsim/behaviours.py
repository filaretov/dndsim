from __future__ import annotations

import random

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Callable


class Behaviour(ABC):
    @abstractmethod
    def pick(self, districts: List[District]) -> District:
        pass


@dataclass
class PreferenceDistrictPicker(Behaviour):
    preferences: List[Callable[[District], float]]

    def pick(self, districts: List[District]) -> District:
        return random.choices(districts, self._weights(districts), k=1)[0]

    def _weights(self, districts: List[District]) -> List[float]:
        return [sum(pref(d) for pref in self.preferences) for d in districts]

@dataclass
class RandomDistrictPicker(Behaviour):
    def pick(self, districts: List[District]) -> District:
        return random.choice(districts)
