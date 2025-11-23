from Node import *

# This method will hold the main loop that goes through our parse tree and calls
# other methods
# def exectutor(trees):
def executor(forest):
    lines = []
    for root in forest:
        arr = inorder(root)
        if not arr:
            continue

        head = arr[0].lower()
        if head == "import":
            lines.append(imports(arr))
        elif head == "function":
            lines.append(start_function(arr))
        elif head == "define":
            lines.append(define(arr))
        elif head == "set":
            lines.append(setting(arr))
        elif head == "display":
            if "," in arr:
                lines.append(displayVar(arr))
            else:
                lines.append(displayString(arr))
        elif head == "endfun":
            lines.append("return 0;")
            lines.append("}")
    return lines

# This takes the inorder array representation for an import and translates it to it's equivalent in C


def imports(tree):
    translated_line = "#include " + tree[1] + ";"
    return translated_line

# We need a method for the starting keywords function, define, display
# (one that handles with variables and one for without, or two options in the same method), set,
# exit, and endfun


def start_function(tree):

    # Scl: function [function name] return typ [datatype] is
    # C: [datatype] [function name]() {

    if tree[4] == "integer":
        datatype = "int"
    else:
       
        datatype = "void"  # assuming "void" as a fallback

    translated_line = "" + datatype + " " + tree[1] + "() {"

    return translated_line

def exit(tree):
    return "return 0;"


def end_function(tree):
    # SCL: endfun [function name]
    # C: }

    translated_line = "}"
    return translated_line


def define(tree): #fixed indexerror
     # ['define', var, 'of', datatype]
    var_name = tree[1]
    datatype = tree[3]      # not tree[4]

    # map SCL types to C types if you want:
    if datatype == "integer":
        c_type = "int"
    elif datatype == "double":
        c_type = "double"
    elif datatype == "char":
        c_type = "char"
    else:
        c_type = "int"  # fallback

    return f"{c_type} {var_name};"

def setting(tree):
    # scl: set [variable name] = [value]
    # c: [variable name] = [value];

    translated_line = "" + tree[1] + " = " + tree[3] + ";"

    return translated_line


def exit_function(): #fixed function already defined error
    translated_line = "return 0;"
    return translated_line


def displayVar(tree):  #assume int and grab the last element as the var name
     # SCL: display "text", x
    string = tree[1]
    var_name = tree[-1]

    return f"printf({string} %d, {var_name});"
    

def displayString(tree):
    # SCL: Display "[String]"
    # C: Printf("[String]")

    translated_line = "printf("+tree[1]+");"
