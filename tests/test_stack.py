from data_structures.stack import *


def test_dunder_str_empty_stack():
    stack = Stack()
    expected = "Stack status: 0 items"
    actual = str(stack)
    assert expected == actual

def test_dunder_str_non_empty_stack():
    stack = Stack(1, 2)
    expected = "Stack status: 2 items"
    actual = str(stack)
    assert expected == actual

def test_dunder_repr_empty_stack():
    stack = Stack()
    expected = "Stack()"
    actual = repr(stack)
    assert expected == actual

def test_dunder_repr_non_empty_stack():
    stack = Stack(1, 2)
    expected = "Stack(1, 2)"
    actual = repr(stack)
    assert expected == actual