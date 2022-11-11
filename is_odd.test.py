from main import is_odd

'''Тестирует на нечетность в диапазоне от 1 до 10'''


def is_odd_test(num):
    odd = [1, 3, 5, 7, 9]
    result = False
    if num in odd:
        result = True
    assert result == is_odd(num)


is_odd_test(3)
is_odd_test(6)
is_odd_test(9)
is_odd_test("asd")
