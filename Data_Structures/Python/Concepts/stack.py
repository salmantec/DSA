"""
Note:

In Python, we can implement stack with help of "LIST". But, the only issue with List, It'll act as a Dynamic array.
Whenever reach the memory limit (let's say after 10 items), It'll move to all the values into new place in memory (10*2).

So, we can use "deque" from collections to implement the stack.


Complexities:

1. Push / Pop element - Constant O(1)
2. Search element     - Linear O(n)
"""


from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


s = Stack()
s.push("https://www.cnn.com")
s.push("https://www.cnn.com/world")
s.push("https://www.cnn.com/india")

print(s.peek())

print(s.pop())

print(s.is_empty())

print(s.size())

print(s.pop())
print(s.pop())

print(s.is_empty())

print(s.size())
