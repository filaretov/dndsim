from dndsim import (
    District,
    Resources,
    PreferenceDistrictPicker,
    FactionAgent,
    QuarterModel,
)

import pytest


@pytest.fixture
def wheat_district():
    return District("The Wheat District", ["wheat"], Resources.ones())


@pytest.fixture
def coal_district():
    return District("The Coal District", ["coal"], Resources.ones())


@pytest.fixture
def wheat_faction():
    want_wheat = lambda d: 1 if "wheat" in d else 0
    return FactionAgent(
        resources=Resources.ones(),
        behaviour=PreferenceDistrictPicker([want_wheat]),
    )


def test_deterministic_single_pair(wheat_district, wheat_faction):
    qm = QuarterModel([wheat_faction], [wheat_district])
    assert qm.step().factions[0].resources == Resources.ones() * 2
    assert qm.step().step().factions[0].resources == Resources.ones() * 3
    assert qm.step().step().step().factions[0].resources == Resources.ones() * 4
