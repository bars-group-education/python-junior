class MyException(Exception):
    pass


def some_func():
    pass


def factorial(number):
    """
    Возвращает факториал переданного числа
    Args:
        number: число, для которого надо посчитать факториал

    Returns:
        product - int - факториал от number
    """
    product = 1
    for element in range(1, number+1):
        product *= element

    return product


FOO = [2, 1, 0, 0]

def specific_func():
    global FOO
    res = FOO.pop()
    assert res
    FOO = [2, 1, 0, 0]

    return res





