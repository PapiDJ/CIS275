from AbstractCollection import AbstractCollection
from BinaryNode import BinaryNode
from LinkedQueue import LinkedQueue


class LinkedBST(AbstractCollection):
	""" A linked binary search tree implementation which uses Nodes """

	def __init__(self):
		self._root = None
		AbstractCollection.__init__(self)

	def find(self, item):
		""" Return data if the item is found or 'None' otherwise """

		def recurse(node):
			if node is None:
				# First Base Case: Item was not found
				return None
			elif item == node.data:
				# Second Base Case: node contains the item!
				return node.data
			elif item < node.data:
				# Recursive Step 1: Move left
				return recurse(node.left)
			else:
				# Recursive Step 2: Move right
				return recurse(node.right)

		return recurse(self._root)

	def add(self, item):
		def recurse(node):
			""" Recursive inner function to find 'item's correct location
			'node' is the root of the tree or subtree being added to """
			if item < node.data:
				# New item being added is less. Go left once if needed
				if node.left is None:
					node.left = BinaryNode(item)
				else:
					recurse(node.left)

			# new item is greater or equal to root, go right if needed
			elif node.right is None:
				node.right = BinaryNode(item)
			else:
				recurse(node.right)

		if self.is_empty():
			# Tree is empty, 'item' becomes the new root
			self._root = BinaryNode(item)
		else:
			# Tree is not empty. Find item's location
			recurse(self._root)

		self._size += 1

	def inorder(self):
		""" Prints the tree with an inorder traversal """
		def recurse(node):
			if node is not None:
				recurse(node.left)
				print(node.data, end=" ")
				recurse(node.right)

		recurse(self._root)

	def postorder(self):
		""" Prints the tree with a postorder traversal """
		def recurse(node):
			if node is not None:
				recurse(node.left)
				recurse(node.right)
				print(node.data, end=" ")

		recurse(self._root)

	def preorder(self):
		""" Prints the tree with a preorder traversal """
		def recurse(node):
			if node is not None:
				print(node.data, end=" ")
				recurse(node.left)
				recurse(node.right)

		recurse(self._root)

	def getSmallest(self):
		""" Since this is a BST, the smallest item is always the leftmost node so that is why we recurse left
			but if no left child exists, then the current node is the smallest, which would be the root node"""
		def recurse(node):
			if node.left is None:
				return node.data
			else:
				return recurse(node.left)

		return recurse(self._root)

	def getLargest(self):
		""" Same goes for the getLargest method, the largest item is always the rightmost node so that is why we recurse right 
			but if no right child exists, then the current node is the largest, which would be the root node """
		def recurse(node):
			if node.right is None:
				return node.data
			else:
				return recurse(node.right)

		return recurse(self._root)

	# I DO NOT BELIEVE THERE IS A BETTER WAY TO WRITE THESE TWO METHODS SO I JUST TRIED TO BEST EXPLAIN WHAT WAS HAPPENING IN THE CODE
	
	def heightBST(self):
		""" Returns the height of the tree """
		def recurse(node):
			if node is None:
				return 0
			else:
				return 1 + max(recurse(node.left), recurse(node.right))

		return recurse(self._root)

	def breadthFirst(self):
		""" FOLLOWED YOUR SUDO CODE """
		q = LinkedQueue()
		q.add(self._root)
		#loop until the queue is empty
		while not q.is_empty():
			#remove the front of the queue
			node = q.pop()
			#print node at front of queue
			print(node.data, end=" ")
			#add the children of the node to the back of the queue
			if node.left is not None:
				q.add(node.left)
			if node.right is not None:
				q.add(node.right)
    
	def is_balanced(self):
		""" Returns True if the tree is balanced and False otherwise """
		def recurse(node):
			if node is None:
				return 0
			else:
				return 1 + max(recurse(node.left), recurse(node.right))
		def recurse2(node):
			if node is None:
				return 0
			else:
				return 1 + min(recurse2(node.left), recurse2(node.right))

		if recurse(self._root) - recurse2(self._root) <= 1:
			return True
		else:
			return False

	def balance(self):
		""" If the tree is balanced, no need to do anything."""
		if self.is_balanced():
			return
		""" Add each item in the tree to a list in sorted order. """
		items = []
		def recurse(node):
			if node is not None:
				recurse(node.left)
				items.append(node.data)
				recurse(node.right)
		recurse(self._root)
		""" Clear the tree. """
		self._root = None
		""" Create a new binary search tree """
		newBST = LinkedBST()
		""" Add the items back to the tree in sorted order. """
		def recurse2(items):
			if len(items) == 0:
				return
			""" We visit the middle by dividing the length of the list by 2"""
			mid = len(items) // 2
			newBST.add(items[mid])
			recurse2(items[:mid])
			recurse2(items[mid+1:])
		recurse2(items)
		""" Set the root of the current tree to the root of the new tree. """
		self._root = newBST._root