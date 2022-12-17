class BinaryNode:
	""" Represents a Node in a binary tree """

	def __init__(self, data, left=None, right=None):
		""" By default, this Node will not have any children """

		self.data = data
		self.left = left
		self.right = right

	def heightBST(self):
		""" I will be recursing through the tree and adding 1 to the max of the left and right children to get the height
			since before I used the height function in my previous code. I will still be using the max function to get the
			maximum height of the left and right children. If the node is None, then I will return 0."""
		def recurse(node):
			if node is None:
				return 0
			else:
				return 1 + max(recurse(node.left), recurse(node.right))

			
