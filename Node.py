from Token import *
#Node Class
class Node:
    def __init__(self, Data):
        self.data= Data
        self.left= None
        self.right= None


# Inorder traversal from the parent node
# inorder_array = []
# fixed inorder_array to return proper result. Initially it would always return only the root node.
def inorder(node):
    
    if node is None:
        return []
    result = []
    if node.left is not None:
        result.extend(inorder(node.left))
    result.append(node.data)
    if node.right is not None:
        result.extend(inorder(node.right))
    return result

#searchs for node and returns the node
def dfs(node, searchNode):
    if node == None:
        return None
    
    if node.data == searchNode:
        return node
    
    searchLeft = dfs(node.left, searchNode)
    if searchLeft != None:
        return searchLeft

    searchRight = dfs(node.right, searchNode)
    if searchRight != None:
        return searchRight


def insertLeft(node, newNode):
    if node.left == None:
        node.left = newNode

def insertRight(node, newNode):
    if node.right == None:
        node.right = newNode

"""
if __name__ == "__main__":
    root = Node(2)
    insertLeft(root, Node(3))
    insertRight(root, Node(4))
    insertLeft(dfs(root, 4), Node(5))
    insertRight(dfs(root, 4), Node(6))

    inorder(root)


    root2= Node(Token("Identifier", "x"))
    insertLeft(root2, Node(Token("Identifier", "y")))

    inorder(root2)

"""
