class Node(object):
	"""
	Class Node for trie.
	"""

	def __init__(self, val):
		self.val = val
		self.children = []
		self.word_end = False


def add(root, word):
	"""
	Adding a word in the trie. We loop through each character through
	the string and create a node and add it to the hierarchy.
	"""
	node = root
	for char in word:
		in_child = False
		for child in node.children:
			if child.val == char:
				node = child
				in_child = True
				break
		if not in_child:
			new_node = Node(char)
			node.children.append(new_node)
			node = new_node

	node.word_end = True


def search(root, word):
	"""
	Method to search a word in trie. We extract each character and
	drill down to the children of current nodes. If found, return true
	else return false
	"""
	node = root
	if not root.children:
		return False
	for char in word:
		word_found = False
		for child in node.children:
			if child.val == char:
				# if word is found, mark word_found to true
				if child.word_end:
					word_found = True
				node = child
				break

	if word_found:
		return True

	return False