from LinkedBST import LinkedBST

t = LinkedBST()
t.add(10)
t.add(5)
t.add(2)
t.add(7)
t.add(15)
t.add(12)
t.add(20)

print(t.getSmallest())
print(t.getLargest())
print(t.heightBST())
print(t.breadthFirst())

r = LinkedBST()
r.add(1)
r.add(5)
r.add(2)
r.add(7)

print(r.is_balanced())
r.balance()
print(r.is_balanced())