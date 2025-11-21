from Node import *

# This method will hold the main loop that goes through our parse tree and calls
# other methods
# def exectutor(trees):

# This takes the inorder array representation for an import and translates it to it's equivalent in C
def imports(tree):
    translated_line = "#include " + tree[1] + ";"
    return translated_line

# We need a method for the starting keywords function, define, display
# (one that handles with variables and one for without, or two options in the same method), set,
# exit, and endfun