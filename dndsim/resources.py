from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Resources:
    money: float = 0
    clergy: float = 0
    law: float = 0
    knowledge: float = 0

    def __add__(self, other: Resources) -> Resources:
        return Resources(
            self.money + other.money,
            self.clergy + other.clergy,
            self.law + other.law,
            self.knowledge + other.knowledge,
        )

    def __mul__(self, mult: float) -> Resources:
        return Resources(
            self.money * mult,
            self.clergy * mult,
            self.law * mult,
            self.knowledge * mult,
        )

    def __eq__(self, other) -> bool:
        return (
            self.money == other.money
            and self.clergy == other.clergy
            and self.law == other.law
            and self.knowledge == other.knowledge
        )

    @classmethod
    def ones(cls) -> Resources:
        return Resources(1, 1, 1, 1)
