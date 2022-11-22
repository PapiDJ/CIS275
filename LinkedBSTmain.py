from LinkedBST import LinkedBST

tree = LinkedBST()

tree.add(5)
tree.add(3)
tree.add(10)
tree.add(2)
tree.add(4)
tree.add(7)
tree.add(12)
tree.add(1)
tree.add(9)
tree.add(11)

if tree.find(12) is not None:
    print(f'Search Complete. {tree._count} nodes visited.')
else:
    print("Search Complete. Item not found.")

tree.postorder()
print("\n")
tree.inorder()
print("\n")
tree.preorder()



