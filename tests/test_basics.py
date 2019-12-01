def test_the_answer():
    from cypack.answer import the_answer

    assert the_answer() == 42


def test_the_wrong_answer():
    from cypack.sub.wrong import the_answer

    assert the_answer() == 13


def test_fibonacci():
    from cypack.fibonacci import fib

    assert fib(7) == 13
