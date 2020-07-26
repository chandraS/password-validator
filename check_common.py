## Phase 1 - Build the trie with the given passwords in weak_password.txt
## Phase 2 - compare the input password with the words in trie and chek if the input password is a common password 

class TrieNode(object):
    """
    Trie node implementation. Starting with initializing a constructor with init function
    """

    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False

## Phase 1 - add function is to build the trie 

def add(root, word: str):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True

## Phase 2 - search function to compare the input against the weak_password list 
    
def search(root, prefix):
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False
    for char in prefix:
        word_found = False
    # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                if child.word_finished:
                    word_found = True
                # Assign node as the child containing the char and break
                node = child
                break

    if word_found:
        print(prefix + ' - Word found in common password')
        return True
    
    return False
