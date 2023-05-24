import pytest
import allure

@allure.title("test_test_skipped")
@pytest.mark.skip
def test_skipped1():
    pass

@allure.title("test_test_skipped")
@pytest.mark.skip
def test_skipped2():
    pass

@allure.title("test_test_skipped")
@pytest.mark.skip
def test_skipped3():
    pass

