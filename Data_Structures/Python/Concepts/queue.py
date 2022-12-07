"""
Check bogocheatsheet.com website to know about the complexities
"""


from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


q = Queue()


q.enqueue({
    'company': 'Wal Mart',
    'timestamp': '15 apr, 11:01 AM',
    'price': 131.10
})

q.enqueue({
    'company': 'Wal Mart',
    'timestamp': '15 apr, 11:02 AM',
    'price': 132.12
})

q.enqueue({
    'company': 'Wal Mart',
    'timestamp': '15 apr, 11:03 AM',
    'price': 135
})


print(q.buffer)
print(q.size())

q.dequeue()

print(q.buffer)
print(q.size())

q.dequeue()

print(q.buffer)
print(q.size())

q.dequeue()

print(q.buffer)
print(q.size())
