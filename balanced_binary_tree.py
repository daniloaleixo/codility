import sys






class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right






least_depth = sys.maxint
max_depth = 0


def update(root, depth):


	global least_depth
	global max_depth

	if (not root.right) and (not root.left):
		if (depth < least_depth): least_depth = depth
		if (depth > max_depth): max_depth = depth

	if(root.left):  update(root.left, depth + 1)
	if(root.right):  update(root.right, depth + 1)



def is_superbalanced(root):


	global least_depth
	global max_depth

	update(root, 0)

	if(max_depth - least_depth > 1):
		return False

	return True


a = BinaryTreeNode(10)
a.insert_right(11)
a.insert_left(9)
a.right.insert_right(12)
a.right.right.insert_right(12)



#print is_superbalanced(a);
print least_depth, max_depth

b = BinaryTreeNode(0)



print is_superbalanced(b);


