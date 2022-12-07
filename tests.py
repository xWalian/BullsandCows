import pytest
from Classes.Dictionary import Dictionary
from Classes.Validator import Validator
from Classes.Stats import Stats
from Classes.Engine import Engine

dic = Dictionary()
val = Validator()
eng = Engine()
stat = Stats()


def test_giveWord():
    assert dic.giveWord is not None


@pytest.mark.parametrize("x, y, z",
                         [("asap", 4, False), ("aszpsd", 5, False), ("asert", 5, True), ("amurebi", 7, True)])
def test_validUserWord(x, y, z):
    assert val.validUserWord(x, y) == z


def test_delStats():
    stat.addCows()
    stat.addBulls()
    stat.delStats()
    assert stat.getCows() == 0 and stat.getBulls() == 0


@pytest.mark.parametrize("x, y, z", [("asap", "asert", False), ("aszpsd", "asert", False), ("asert", "asert", True),
                                     ("amurebi", "amurebi", True)])
def test_validIfWon(x, y, z):
    assert val.validIfWon(x, y) == z


@pytest.mark.parametrize("x, y", [(3, 3), (4, 4), (2, 2)])
def test_setDifficulty(x, y):
    eng.setDifficulty(x)
    assert eng.getDifficulty() == y

@pytest.mark.parametrize("x, y", [(6, 6), (10, 10), (12, 12)])
def test_setTries(x, y):
    eng.setTries(x)
    assert eng.getTries() == y
