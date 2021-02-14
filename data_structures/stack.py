"""
Python implementation of a stack data structure, which is 
LIFO (Last In First Out) behavior.

Methods:
1. push(<item>) onto stack
2. pop(<item>) onto stack
3. isEmpty() checks to see if stack is empty
"""


class Stack:

    def __init__(self, *args):
        if args:
            self.items = [arg for arg in args]
        else:
            self.items = []
        
    def push(self, item: int):
        self.items.push(item)

    def pop(self):
        self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return f"Stack status: {len(self.items)} items"

    def __repr__(self):
        return f"Stack({', '.join(str(x) for x in self.items)})"
