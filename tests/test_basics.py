def test_the_answer():
    from cypack.answer import the_answer

    assert the_answer() == 42


def test_the_wrong_answer():
    from cypack.sub.wrong import the_answer

    assert the_answer() == 13
