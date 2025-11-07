from calculator.src.service import CalculatorService


def test_basic_operations():
    svc = CalculatorService()
    assert svc.evaluate("1 + 2") == 3
    assert svc.evaluate("2 * (3 + 4)") == 14
    assert svc.evaluate("10 / 2") == 5
    assert svc.evaluate("2 ** 3") == 8


def test_history():
    svc = CalculatorService()
    svc.evaluate("1+1")
    svc.evaluate("2+2")
    hist = svc.get_history()
    assert len(hist) >= 2
    assert hist[0].expression == "2+2"
