import os
import sys
from scl_interpreter import scanner 
from Node import *


# Group: Alex Tidwell, Jennifer Morales, Sydney Forbes
"""
We chose to write a parser for the subset of SCL grammar that only allows imports,
defining of variables, the main method, basic arithmetic including addition, subtraction,
multiplication, and division, and displaying a string or variable to the screen.
This parser does not cover other methods, arrays, and anything not listed above.
"""

# gets the next token
def get_next_token(token, tokens):
    token_keys = list(tokens.keys())
    index_of_token = token_keys.index(token)
    if(index_of_token + 1 < len(token_keys)):
        return token_keys[index_of_token + 1]
    else:
        return None
    
identifiers = []

# Checks if an identifier has already been defined
def identifier_present(identifier):
    global identifiers
    if(identifier not in identifiers):
        identifiers.append(identifier)
        return False
    else:
        return True

current = ''
trees = []
# Starts the parsing and returns an array of trees
def start(tokens):
    global current
    global trees
    token_keys = list(tokens.keys())
    current = token_keys[0]
    if(tokens[current]['type'] == 'IMPORT'):
        trees.append(Node("IMPORTS"))
        __imports(current, tokens)
    else:
        print("SYNTAX ERROR 42")
        return None
    if(tokens[current]['type'] == 'IMPLEMENTATIONS'):
        trees.append(Node("IMPLEMENTATIONS"))
        while(tokens[current]['type'] != 'BEGIN'):
            __implementations(current, tokens)
    else:
        print("SYNTAX ERROR 52")
        return None
    if(tokens[current]['type'] == 'BEGIN'):
        trees.append(Node("BEGIN"))
        while(tokens[current]['type'] != 'EXIT'):
            to_break = __begin(current, tokens)
            if(to_break == None):
               break
        end_fun_node = Node('endfun')
        end_fun_node.left = Node('exit')
        end_fun_node.right = Node('main')
        trees.append(end_fun_node)
    else:
        print("SYNTAX ERROR 66")
        return None
    return trees
        
            

# Function that checks syntax on imports and generates AST for them
def __imports(token, tokens):
    global current
    global trees
    node = Node(tokens[token]['value'])
    next_token = get_next_token(token,tokens)
    if(tokens[token]['type'] == 'IMPORT' and tokens[next_token]['type'] == 'STRING'):
        node.right = Node(tokens[next_token]['value'])
        token_after_next = get_next_token(next_token,tokens)
        if(tokens[token_after_next]['type'] == "EOS"):
            trees.append(node)
            next_token = get_next_token(token_after_next, tokens)
            current = next_token
            if(tokens[next_token]['type'] == "IMPORT"):
                __imports(next_token, tokens)
    else:
        print("SYNTAX ERROR! 91")
        return None

# Function that checks syntax on implementations and generates AST for them
def __implementations(token,tokens):
    global current
    global implementation_trees
    global trees
    next_token = get_next_token(token,tokens)
    if(tokens[next_token]['type'] != 'EOS' and tokens[next_token]['type'] != 'DEFINE'):
        print("SYNTAX ERROR 100")
        return None
    token_after_next = get_next_token(next_token, tokens)
    if(tokens[token_after_next]['type'] == 'FUNCTION'):
        next_token = get_next_token(token_after_next, tokens)
        if(tokens[next_token]['type'] == "MAIN"):
            main_head = Node(tokens[next_token]['value'])
            main_head.left = Node(tokens[token_after_next]['value'])
            token_after_next = get_next_token(next_token, tokens)
            if(tokens[token_after_next]['type'] == 'RETURN'):
                next_token = get_next_token(token_after_next,tokens)
                if(tokens[next_token]['type'] == 'TYPE'):
                    current_node = Node(tokens[next_token]['value'])
                    current_node.left = Node(tokens[token_after_next]['value'])
                    main_head.right = current_node
                    token_after_next = get_next_token(next_token,tokens)
                    if(tokens[token_after_next]['type'] == 'INTEGER'):
                        next_token = get_next_token(token_after_next,tokens)
                        if(tokens[next_token]['type'] == 'IS'):
                            next_node = Node(tokens[next_token]['value'])
                            next_node.left = Node(tokens[token_after_next]['value'])
                            current_node.right = next_node
                            token_after_next = get_next_token(next_token,tokens)
                            if(tokens[token_after_next]['type'] == 'EOS'):
                                trees.append(main_head)
                                next_token = get_next_token(token_after_next,tokens)
                                current = next_token
                                if(tokens[next_token]['type'] == 'VARIABLES'):
                                    __data_declarations(next_token, tokens)
                                elif(tokens[next_token]['type'] == 'BEGIN'):
                                    return
                                else:
                                    print("SYNTAX ERROR 133")
                                    return None
                            else:
                                print("SYNTAX ERROR 136")
                                return None
                        else:
                            print("SYNTAX ERROR 139")
                            return None
                    else:
                        print("SYNTAX ERROR 142")
                        return None
                else:
                    print("SYNTAX ERROR 145")
                    return None
            else:
                print("SYNTAX ERROR 148")
                return None
        else:
            print("SYNTAX ERROR 151")
            return None
    else:
        print("SYNTAX ERROR 154")
        return None


# Function that checks syntax on data declarations and generates AST for them
def __data_declarations(token, tokens):
    global current
    global data_trees
    global trees
    next_token = get_next_token(token, tokens)
    if(tokens[next_token]['type'] != 'EOS'):
        print("SYNTAX ERROR 164")
        return None
    next_token = get_next_token(next_token,tokens)
    if(tokens[next_token]['type'] == 'DEFINE'):
        token_after_next = get_next_token(next_token,tokens)
        if(tokens[token_after_next]['type'] == 'IDENTIFIER'):
            present = identifier_present(tokens[token_after_next]['value'])
            if(present):
                print("SYNTAX ERROR. IDENTIFIER ALREADY CREATED")
                return None
            data_head = Node(tokens[token_after_next]['value'])
            data_head.left = Node(tokens[next_token]['value'])
            next_token = get_next_token(token_after_next, tokens)
            if(tokens[next_token]['type'] == 'OF'):
                token_after_next = get_next_token(next_token,tokens)
                if(tokens[token_after_next]['type'] == 'TYPE'):
                    current_node = Node(tokens[token_after_next]['value'])
                    current_node.left = Node(tokens[next_token]['value'])
                    data_head.right = current_node
                    next_token = get_next_token(token_after_next, tokens)
                    if(tokens[next_token]['type'] == 'DOUBLE' or tokens[next_token]['type'] == 'INTEGER' 
                       or tokens[next_token]['type'] == 'CHAR'):
                        current_node.right = Node(tokens[next_token]['value'])
                        trees.append(data_head)
                        token_after_next = get_next_token(next_token,tokens)
                        if(tokens[token_after_next]['type'] == 'EOS'):
                            next_token = get_next_token(token_after_next, tokens)
                            if(tokens[next_token]['type'] == 'DEFINE'):
                                current = next_token
                                __data_declarations(next_token, tokens)
                            else:
                                current = next_token
                        else:
                            print("SYNTAX ERROR 194") 
                            return None
                    else:
                        print("SYNTAX ERROR 197") 
                        return None
                else:
                    print("SYNTAX ERROR 200") 
                    return None            
            else:
                print("SYNTAX ERROR 203") 
                return None
    else:
        print("SYNTAX ERROR 206")
        return None

# Function that checks syntax on things inside the main method and generates AST for them
def __begin(token, tokens):
    global current
    global trees
    next_token = get_next_token(token, tokens)
    if(tokens[next_token]['type'] == 'EOS'):
        token_after_next = get_next_token(next_token,tokens)
    else:
        token_after_next = token
    if(tokens[token_after_next]['type'] == 'DISPLAY'):
        next_token = get_next_token(token_after_next, tokens)
        if(tokens[next_token]['type'] == 'STRING'):
            display_head = Node(tokens[next_token]['value'])
            display_head.left = Node(tokens[token_after_next]['value'])
            token_after_next = get_next_token(next_token,tokens)
            if(tokens[token_after_next]['type'] == 'COMMA'):
                next_token = get_next_token(token_after_next, tokens)
                if(tokens[next_token]['type'] == 'IDENTIFIER'):
                    current_node = Node(tokens[next_token]['value'])
                    current_node.left = Node(tokens[token_after_next]['value'])
                    display_head.right = current_node
                    token_after_next = get_next_token(next_token,tokens)
                    if(tokens[token_after_next]['type'] == 'EOS'):
                        trees.append(display_head)
                        next_token = get_next_token(token_after_next, tokens)
                        if(tokens[next_token]['type'] == 'SET' or 
                           tokens[next_token]['type'] == 'DISPLAY'):
                            current = next_token
                            __begin(next_token, tokens)
                        elif(tokens[next_token]['type'] == 'EXIT'):
                            trees.append(Node('exit'))
                            return 
                    else:
                        print("SYNTAX ERROR 240")
                        return None
                else:
                    print("SYNTAX ERROR 243")
                    return None
            elif(tokens[token_after_next]['type'] == 'EOS'):
                next_token = get_next_token(token_after_next, tokens)
                current = next_token
                trees.append(display_head)
                if(tokens[next_token]['type'] == 'DISPLAY' or
                   tokens[next_token]['type'] == 'SET'):
                    __begin(next_token, tokens)
                elif(tokens[next_token]['type'] == 'EXIT'):
                    trees.append(Node('exit'))
                    return 
            else:
                print("SYNTAX ERROR 256")
                return None
        else:
            print("SYNTAX ERROR 259")
            return None
    elif(tokens[token_after_next]['type'] == 'SET'):
        next_token = get_next_token(token_after_next, tokens)
        if(tokens[next_token]['type'] == 'IDENTIFIER'):
            set_head = Node(tokens[next_token]['value'])
            set_head.left = Node(tokens[token_after_next]['value'])
            token_after_next = get_next_token(next_token,tokens)
            if(tokens[token_after_next]['type'] == 'EQUALS'):
                next_expr = Node(tokens[token_after_next]['value'])
                set_head.right = next_expr
                next_token = get_next_token(token_after_next, tokens)
                if(tokens[next_token]['type'] == 'IDENTIFIER' or 
                   tokens[next_token]['type'] == 'NUM'):
                    token_after_next = get_next_token(next_token,tokens)
                    if(tokens[token_after_next]['type'] == 'EOS'):
                        current = next_token
                        next_expr.right = Node(tokens[next_token]['value'])
                        trees.append(set_head)
                    elif(tokens[token_after_next]['type'] == 'PLUS' or
                         tokens[token_after_next]['type'] == 'MINUS' or
                         tokens[token_after_next]['type'] == 'STAR' or
                         tokens[token_after_next]['type'] == 'DIVOP'):
                        current = next_token
                        next_expr.right = __expressions(next_token, tokens)
                        trees.append(set_head)
            else:
                print("SYNTAX ERROR 277")
                return None
        else:
            print("SYNTAX ERROR 280")
            return None
    elif(tokens[token_after_next]['value'] == 'EXIT'):
        current = token_after_next
        trees.append(Node('exit'))
        return
    else:
        print("SYNTAX ERROR 287")
        return None
    
# Function that checks syntax on expressions with + or - and generates AST for them
def __expressions(token, tokens):
    global current
    next_token = get_next_token(token, tokens)
    if(tokens[next_token]['type'] == 'PLUS' or 
       tokens[next_token]['type'] == 'MINUS'):
        token_after_next = get_next_token(next_token,tokens)
        if(tokens[token_after_next]['type'] == 'NUM' or
           tokens[token_after_next]['type'] == 'IDENTIFIER'):
            expr_head = Node(tokens[next_token]['value'])
            expr_head.left = Node(tokens[token]['value'])
            next_token = get_next_token(token_after_next, tokens)
            current = next_token
            if(tokens[next_token]['type'] == 'PLUS' or
               tokens[next_token]['type'] == 'MINUS'):
                expr_head.right = __expressions(token_after_next, tokens)
                return expr_head
            elif(tokens[next_token]['type'] == 'STAR' or
                tokens[next_token]['type'] == 'DIVOP'):
                expr_head.right = __expressions_other(token_after_next, tokens)
                return expr_head
            elif(tokens[next_token]['type'] == 'EOS'):
                token_after_next = get_next_token(next_token, tokens)
                current = token_after_next
                expr_head.right = Node(tokens[token_after_next]['value'])
                return expr_head
            else:
                print("SYNTAX ERROR 318")
                return None
        else:
            print("SYNTAX ERROR 321")
            return None
    elif(tokens[next_token]['type'] == 'STAR' or 
       tokens[next_token]['type'] == 'DIVOP'):
        current = next_token
        expr_head = __expressions_other(token, tokens)
        return expr_head
    elif(tokens[next_token]['type'] == 'EXIT'):
        current = next_token
        __begin(next_token,tokens)
    else:
        print("SYNTAX ERROR 332")
        return None
            
# Function that checks syntax on expressions with * or / and generates AST for them    
def __expressions_other(token,tokens):
    global current
    next_token = get_next_token(token, tokens)
    current = next_token
    if(tokens[next_token]['type'] == 'STAR' or 
       tokens[next_token]['type'] == 'DIVOP'):
        token_after_next = get_next_token(next_token,tokens)
        if(tokens[token_after_next]['type'] == 'NUM' or
           tokens[token_after_next]['type'] == 'IDENTIFIER'):
            expr_head = Node(tokens[next_token]['value'])
            expr_head.left = Node(tokens[token]['value'])
            next_token = get_next_token(token_after_next, tokens)
            current = next_token
            if(tokens[next_token]['type'] == 'STAR' or
               tokens[next_token]['type'] == 'DIVOP'):
                expr_head.right = __expressions_other(token_after_next, tokens)
                return expr_head
            elif(tokens[next_token]['type'] == 'PLUS' or
                tokens[next_token]['type'] == 'MINUS'):
                expr_head.right = __expressions(token_after_next, tokens)
                return expr_head
            elif(tokens[next_token]['type'] == 'EOS'):
                token_after_next = get_next_token(next_token, tokens)
                current = token_after_next
                expr_head.right = Node(tokens[token_after_next]['value'])
                return expr_head
            else:
                print("SYNTAX ERROR 360")
                return None
        else:
            print("SYNTAX ERROR 363")
            return None
    else:
        print("SYNTAX ERROR 366")


commandLine = sys.argv #What is inputted into the CLI

# Main method
if __name__ == "__main__":
    if len(commandLine) < 1:
        print("Usage: python parser.py <file.scl>")
        sys.exit(1)

    src_path = "SCL/" + commandLine[1]

    if not os.path.exists(src_path):
        print(f"Error: file not found: {src_path}")
        sys.exit(1)

    tokens = scanner(str(src_path))

    forest = []
    forest = start(tokens)

    for tree in forest:
        print(inorder(tree))



            
