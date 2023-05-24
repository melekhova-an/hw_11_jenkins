import allure

@allure.title("test_fail")
def test_fail1():
    assert False

def test_fail2():
    assert False

@allure.title("test_fail")
def test_fail3():
    assert False

@allure.title("test_fail")
def test_fail4():
    assert False

@allure.title("test_fail")
def test_fail5():
    assert False

@allure.title("test_fail5")
def test_fail6():
    assert False
