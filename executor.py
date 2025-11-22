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

def start_function(tree):
    #function main return typ integer is -> int main() {
    #Scl: function [function name] return typ [datatype] is
    #C: [datatype] [function name]() {

    if tree[4] == "integer" :
        datatype="int"

    translated_line= "" + datatype + " " + tree[1] + "(){"
    
    return translated_line 

def exit(tree):
    return "return 0;"

def end_function(tree):
    #SCL: endfun [function name]
    #C: }

    translated_line ="}"
    return translated_line

def define(tree):
    #scl: define [variable] of type [datastype]
    #C: [datatype] [variable];

    translated_line ="" + tree[4] +" " + tree[1] +";"

    return translated_line

def setting(tree):
    #scl: set [variable name] = [value] 
    #c: [variable name] = [value];

    translated_line ="" + tree[1] + " = " + tree[3] + ";"

    return translated_line

def exit():
    translated_line="return 0;"
    return translated_line


def displayVar(varDict, tree):
    #SCL: display "Value of x: ", x 
    #C: printf("Value of x: %f", x);
    #C: printf([String] %[var datatype], [variable]);

    
    if type(varDict[tree[4]])==float:
        datatype="f"
    elif type(varDict[tree[4]])==int:
        datatype="d" 

    translated_line= "printf("+tree[1] +"%"+datatype+", "+tree[4] + ");"
    return translated_line
    

def displayString(tree):
    #SCL: Display "[String]"
    #C: Printf("[String]")

    translated_line="printf("+tree[1]+");"
    
