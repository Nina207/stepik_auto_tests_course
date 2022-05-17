import pytest

@pytest.mark.xfail(strict="неожжиданно упавший тест")
def test_succeed():
    assert True

@pytest.mark.xfail
def test_not_succed():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False
