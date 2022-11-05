from main import calculate


def test(a, b):
    c = calculate(a, b)
    result = a + b
    assert c == result


test(10, 20)
test(5, 20)
test(10, 10)
