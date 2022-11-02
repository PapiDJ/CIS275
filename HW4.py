from ArrayQueue import ArrayQueue

q = ArrayQueue()

q.add(1)
q.add(3)
q.add(5)
q.add(8)
q.add(4)
q.add(0)
q.add(7)
q.add(2)
q.add(9)
q.add(6)

print(q)
print(q.is_empty())

q.pop()
print(q.peek())
print(q)

q.add(1)

print(q)



