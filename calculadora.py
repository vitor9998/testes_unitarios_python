# assert é para outros desenvolvedores.
# Não vai utilizar assertion para seu usuário final.

def soma(x, y):
    # assert -> to afirmando x é int ou float.
    '''
    >>> soma(10, 20)
    30
    >>> soma(-10, 20)
    10
    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    '''
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(x, (int, float)), 'y precisa ser int ou float'
    return x + y


def subtrai(x, y):
    """Subtrai x e y

    >>> subtrai(10, 5)
    5

    >>> subtrai('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float

    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(x, (int, float)), 'y precisa ser int ou float'
    return x - y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


# No ipython consigo fazer esses ex:
# from calculadora import soma
# soma(10,20)



