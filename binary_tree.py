class binaryTreeNode:
	def __init__(self, value):
		self.value = value
		self.left_child_node = None
		self.right_child_node = None

class myBinaryTree:
	def __init__(self):
		self.root_node = None

	def add(self, value):
		# add the value into the tree.
		
		# if no root node then set value to root

		if self.root_node == None:
			self.root_node = binaryTreeNode(value)
			return


		if value > self.root_node.value:
			self.root_node.right_child_node = binaryTreeNode(value)
		else:
			self.root_node.left_child_node = binaryTreeNode(value)

		# for i in self.left_child_node:
		# 	for j in self.right_child_node:
		# 		while value > i:

#########################################################
		current_node = self.root_node
		# loop by assigning current node over and over again
		while current_node != None:
            if value >= current_node.value:
                if current_node.right_child_node == None:
                    current_node.right_child_node = BinaryTreeNode(value)
                    break
                else:
                    current_node = current_node.right_child_node
            else:
                if current_node.left_child_node == None:
                    current_node.left_child_node = BinaryTreeNode(value)
                    break
                else:
                    current_node = current_node.left_child_node
			


b = myBinaryTree()
b.add(10)
b.add(11)