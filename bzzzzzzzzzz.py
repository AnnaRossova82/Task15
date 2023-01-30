import unittest
def inc(x):
    return x + 1


def add(a, b):
    return a + b


def test_answer():
    assert inc(4) == 5


def test_answer2():
    assert inc(2) == 3


def test_add(x1, x2, answer):
    assert add(x1, x2) == answer
    print('test for function add is passed')


test_answer()
test_answer2()
test_add(2, 7, 9)
test_add(43, 57, 100)

def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_answer():
    self.assertIsInstance(a, b)
