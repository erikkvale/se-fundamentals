from data_structures.stack import *

# Tests for dunder methods
def test_dunder_init_with_no_args():
    stack = Stack()
    expected = 0
    actual = len(stack.items)
    assert expected == actual

def test_dunder_init_with_args():
    stack = Stack(1, 2)
    expected = 2
    actual = len(stack.items)
    assert expected == actual

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
