import pytest

from dndsim.behaviours import PreferenceDistrictPicker, RandomDistrictPicker
from dndsim import FactionAgent, District, Resources


@pytest.fixture
def districts():
    """I am obviously a creative person."""
    a = District("a", ["coal"], Resources.ones() * 0.5)
    b = District("b", ["temple"], Resources.ones() + Resources(law=1))
    c = District("c", ["shipyard"], Resources.ones() + Resources(money=1))
    return [a, b, c]


@pytest.fixture
def preferences():
    base = lambda _d: 1
    want_coal = lambda d: 2 if "coal" in d else 0
    want_law = lambda d: 2 if d.resources.law > 1 else 0
    return [base, want_coal, want_law]


@pytest.fixture
def district():
    return District("", [], Resources.ones())


@pytest.fixture
def resources():
    return Resources.ones()

@pytest.fixture
def faction():
    return FactionAgent(
        Resources.ones(),
        RandomDistrictPicker(),
        name="The Wheat Faction",
    )


def test_district(district):
    """I know, I know, I should test something meaningful."""
    assert len(district.poi) == 0
    assert district.resources == Resources.ones()


def test_resources_math():
    assert Resources.ones() + Resources.ones() == Resources(2, 2, 2, 2)
    assert Resources.ones() * 10 == Resources(10, 10, 10, 10)


def test_picker(districts, preferences):
    """The _weights method isn't meant for public use, but it's much easier to
    test than the pick method.  pick only samples from the districts using
    stdlib random, so there's not much to test anyway.

    TODO: Create a more readable fixture that combines `districts` and `preferences`,
    the [3, 3, 1] weight list is too magic-number-y.
    """
    pdp = PreferenceDistrictPicker(preferences)
    assert pdp._weights(districts) == [3, 3, 1]


def test_faction_equality(faction):
    faction_incr = FactionAgent(faction.resources * 2, RandomDistrictPicker(), faction.name)
    assert faction == faction_incr
    assert hash(faction) == hash(faction_incr)
