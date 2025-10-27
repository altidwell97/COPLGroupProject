import os
import sys
from scl_interpreter import scanner 
from Node import *




def get_next_token(token, tokens):
    token_keys = list(tokens.keys())
    index_of_token = token_keys.index(token)
    if(index_of_token + 1 < len(token_keys)):
        return token_keys[index_of_token + 1]
    else:
        return None
    
identifiers = []

def identifier_present(identifier):
    if(identifier not in identifiers):
        identifiers.append(identifier)
        return False
    else:
        return True

current = ''
def start(tokens):
    global current
    token_keys = list(tokens.keys())
    more_tokens = True
    current = token_keys[0]
    trees = []
    while(more_tokens):
        if(tokens[current]['type'] == 'IMPORT'):
            trees.append(Node("IMPORTS"))
            trees_returned = imports(current, tokens)
            if(trees_returned == None):
                break
            else:
                trees.append(trees_returned)
        else:
            print("SYNTAX ERROR 42")
            break
        if(tokens[current]['type'] == 'IMPLEMENTATIONS'):
            trees.append(Node("IMPLEMENTATIONS"))
            trees_returned = implementations(current, tokens)
            if(trees_returned == None):
                break
            else:
                trees.append(trees_returned)
        else:
            print("SYNTAX ERROR 52")
            break
        if(tokens[current]['type'] == 'BEGIN'):
            trees.append(Node("BEGIN"))
            while(current != 'Exit'):
                trees_returned = begin(current, tokens)
                if(trees_returned == None):
                    break
                else:
                    trees.append(trees_returned)
            end_fun_node = Node('endfun')
            end_fun_node.right = Node('main')
            trees.append(end_fun_node)
        else:
            print("SYNTAX ERROR 66")
            break
        return trees
        
            

import_trees = []
def imports(token, tokens):
    global current
    global import_trees
    node = Node(tokens[token]['value'])
    next_token = get_next_token(token,tokens)
    if(tokens[token]['type'] == 'IMPORT' and tokens[next_token]['type'] == 'STRING'):
        node.right = Node(tokens[next_token]['value'])
        token_after_next = get_next_token(next_token,tokens)
        if(tokens[token_after_next]['type'] == "EOS"):
            import_trees.append(node)
            next_token = get_next_token(token_after_next, tokens)
            current = next_token
            if(tokens[next_token]['type'] == "IMPORT"):
                imports(next_token, tokens)
                return import_trees
            else:
                return import_trees
    else:
        print("SYNTAX ERROR! 91")
        return None

implementation_trees = []
def implementations(token,tokens):
    global current
    global implementation_trees
    next_token = get_next_token(token,tokens)
    if(tokens[next_token]['type'] != 'EOS'):
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
                next_token = get_next_token(next_token,tokens)
                if(tokens[next_token]['type'] == 'TYPE'):
                    current_node = Node(tokens[next_token]['value'])
                    current_node.left = Node(tokens[token_after_next]['value'])
                    main_head.right = current_node
                    token_after_next = get_next_token(token_after_next,tokens)
                    if(tokens[token_after_next]['type'] == 'INTEGER'):
                        next_token = get_next_token(next_token,tokens)
                        if(tokens[next_token]['type'] == 'IS'):
                            next_node = Node(tokens[next_token]['value'])
                            next_node.left = Node(tokens[token_after_next]['value'])
                            current_node.right = next_node
                            token_after_next = get_next_token(token_after_next,tokens)
                            if(tokens[token_after_next]['type'] == 'EOS'):
                                implementation_trees.append(main_head)
                                next_token = get_next_token(next_token,tokens)
                                current = next_token
                                if(tokens[next_token]['type'] == 'VARIABLES'):
                                    data_declarations(next_token, tokens)
                                    return implementation_trees
                                elif(tokens[next_token]['type'] == 'BEGIN'):
                                    return implementation_trees
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


data_trees = []
def data_declarations(token, tokens):
    global current
    global data_trees
    next_token = get_next_token(token, tokens)
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
                    next_token = get_next_token(token_after_next, tokens)
                    if(tokens[next_token]['type'] == 'DOUBLE' or tokens[next_token]['type'] == 'INTEGER' 
                       or tokens[next_token]['type'] == 'CHAR'):
                        current_node.right = Node(tokens[next_token]['value'])
                        data_trees.append(data_head)
                        token_after_next = get_next_token(next_token,tokens)
                        if(tokens[token_after_next]['type'] == 'EOS'):
                            next_token = get_next_token(token_after_next, tokens)
                            if(tokens[next_token]['type'] == 'DEFINE'):
                                current = next_token
                                data_declarations(next_token, tokens)
                                return(data_trees)
                            else:
                                current = next_token
                                return data_trees
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
    
begin_trees = []
def begin(token, tokens):
    global current
    global begin_trees
    next_token = get_next_token(token, tokens)
    if(tokens[next_token]['type'] == 'EOS'):
        token_after_next = get_next_token(next_token,tokens)
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
                            begin_trees.append(display_head)
                            next_token = get_next_token(token_after_next, tokens)
                            if(tokens[next_token]['type'] == 'SET' or 
                               tokens[next_token]['type'] == 'DISPLAY'):
                                current = next_token
                                begin(next_token, tokens)
                            elif(tokens[next_token]['type'] == 'EXIT'):
                                begin_trees.append(Node('exit'))
                                return begin_trees
                        else:
                            print("SYNTAX ERROR 240")
                            return None
                    else:
                        print("SYNTAX ERROR 243")
                        return None
                elif(tokens[token_after_next]['type'] == 'EOS'):
                    next_token = get_next_token(token_after_next, tokens)
                    current = next_token
                    begin_trees.append(display_head)
                    if(tokens[next_token]['type'] == 'DISPLAY' or
                       tokens[next_token]['type'] == 'SET'):
                        begin(next_token, tokens)
                    elif(tokens[next_token]['type'] == 'EXIT'):
                        begin_trees.append(Node('exit'))
                        return begin_trees
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
                    set_head.right = Node(tokens[token_after_next]['value'])
                    next_token = get_next_token(token_after_next, tokens)
                    if(tokens[next_token]['type'] == 'IDENTIFIER' or 
                       tokens[next_token]['type'] == 'NUM'):
                        current = next_token
                        next_expr = set_head.right
                        next_expr.right = expressions(next_token, tokens)
                        begin_trees.append(set_head)
                else:
                    print("SYNTAX ERROR 277")
                    return None
            else:
                print("SYNTAX ERROR 280")
                return None
        elif(tokens[token_after_next]['value'] == 'EXIT'):
            current = token_after_next
            begin_trees.append(Node('exit'))
            return begin_trees
        else:
            print("SYNTAX ERROR 287")
            return None

    else:
        print("SYNTAX ERROR 291")
        return None

def expressions(token, tokens):
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
                expr_head.right = expressions(token_after_next, tokens)
            elif(tokens[next_token]['type'] == 'STAR' or
                tokens[next_token]['type'] == 'DIVOP'):
                expr_head.right = expressions_other(token_after_next, tokens)
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
        expr_head = expressions_other(token, tokens)
        return expr_head
    elif(tokens[next_token]['type'] == 'EXIT'):
        current = next_token
        begin(next_token,tokens)
    else:
        print("SYNTAX ERROR 332")
            
    
def expressions_other(token,tokens):
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
                expr_head.right = expressions_other(token_after_next, tokens)
            elif(tokens[next_token]['type'] == 'PLUS' or
                tokens[next_token]['type'] == 'MINUS'):
                expr_head.right = expressions(token_after_next, tokens)
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
    forest.append(start(tokens))

    for tree in forest:
        #in_order = 
        inorder(tree)
        #print(in_order)



            
