import os
import sys
import json
from scl_interpreter import scanner 




def get_next_token(token, tokens):
    token_keys = list(tokens.keys())
    index_of_token = token_keys.index(token)
    if(index_of_token + 1 < len(token_keys)):
        # CONSIDER TRYING
        # MAY NOT WORK SINCE NEED TO KEEP TRACK FO CURRENT TOKEN
        # CAN TRY BY HAVING CURRENT KEEP TRACK OF INDEX AGAIN
        # next_token = token_keys[index_of_token + 1]
        # return tokens[next_token]
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
def start(tokens, trees):
    global current
    token_keys = list(tokens.keys())
    more_tokens = True
    current_token = token_keys[current]
    current = token_keys[0]
    while(more_tokens):
        # if(tokens[token_keys[current]]['type'] == 'IMPORT'):
        if(tokens[current]['type'] == 'IMPORT'):
            import_head = 
            trees.append(imports(tokens[token_keys[current]], tokens, import_head))
            if(trees[0] == None):
                break
        else:
            print("SYNTAX ERROR")
            break
        # elif(tokens[token_keys[current]]['type'] == 'IMPLEMENTATIONS'):
        if(tokens[current]['type'] == 'IMPLEMENTATIONS'):
            implementations_head = 
            trees.append(implementations(tokens[token_keys[current]], tokens, implementations_head))
            if(trees[1] == None):
                break
        else:
            print("SYNTAX ERROR")
            break
        if(tokens[current]['type'] == 'BEGIN'):
            begin_head = 
            trees.append(begin(tokens[token_keys[current]], tokens, begin_head))
            if(trees[2] == None):
                break
        else:
            print("SYNTAX ERROR")
            break
        return trees
            


def imports(token, tokens, node):
    global current
    import_tree_nodes = []
    next_token = get_next_token(token,tokens)
    if(token['type'] == 'IMPORT' and tokens[next_token]['type'] == 'STRING'):
        import_tree_nodes.append(tokens[token]['value'])
        import_tree_nodes.append(tokens[next_token]['value'])
        token_after_next = get_next_token(next_token,tokens)
        if(tokens[token_after_next]['type'] == "EOS"):
            next_token = get_next_token(token_after_next, tokens)
            if(tokens[next_token]['type'] == "IMPORT"):
                import_tree_nodes.append(tokens[token_after_next]['value'])
                import_tree_nodes.append(imports(next_token, tokens))
            else:
                return import_tree_nodes
    else:
        print("SYNTAX ERROR!")
        return None


def implementations(token,tokens, node):
    global current
    next_token = get_next_token(token,tokens)
    if(tokens[next_token]['type'] != 'EOS'):
        print("SYNTAX ERROR")
        return None
    token_after_next = get_next_token(next_token, tokens)
    if(tokens[token_after_next]['type'] == 'FUNCTION'):
        next_token = get_next_token(token_after_next, tokens)
        if(tokens[next_token]['type'] == "MAIN"):
            node. = main_head(next_token, tokens, node)
            if(node. == None):
                return None
            else:
                return node
        else:
            print("SYNTAX ERROR")
            return None
    else:
        print("SYNTAX ERROR")
            return None

        
def main_head(token, tokens, node):
    global current
    next_token = get_next_token(token, tokens)
    if(tokens[next_token]['type'] == 'RETURN'):
        token_after_next = get_next_token(next_token,tokens)
        if(tokens[token_after_next]['type'] == 'TYPE'):
            next_token = get_next_token(token_after_next,tokens)
            if(tokens[next_token]['type'] == 'INTEGER'):
                token_after_next = get_next_token(next_token,tokens)
                if(tokens[token_after_next]['type'] == 'IS'):
                    next_token = get_next_token(token_after_next,tokens)
                    if(tokens[next_token]['type'] == 'EOS'):
                        token_after_next = get_next_token(next_token,tokens)
                        if(tokens[token_after_next]['type'] == 'VARIABLES'):
                            node. = data_declarations(token_after_next, tokens, node)
                            return node
                    else:
                        print("SYNTAX ERROR")
                        return None
                else:
                    print("SYNTAX ERROR")
                    return None
            else:
                print("SYNTAX ERROR")
                return None
        else:
            print("SYNTAX ERROR")
            return None
    else:
        print("SYNTAX ERROR")
        return None
    
def data_declarations(token, tokens, node):
    global current
    next_token = get_next_token(token, tokens)
    if(tokens[next_token]['type'] == 'DEFINE'):
        token_after_next = get_next_token(next_token,tokens)
        if(tokens[token_after_next]['type'] == 'IDENTIFIER'):
            present = identifier_present(tokens[token_after_next]['value'])
            if(present):
                print("SYNTAX ERROR. IDENTIFIER ALREADY CREATED")
                return None
            next_token = get_next_token(token_after_next, tokens)
            if(tokens[next_token]['type'] == 'OF'):
                token_after_next = get_next_token(next_token,tokens)
                if(tokens[token_after_next]['type'] == 'TYPE'):
                    next_token = get_next_token(token_after_next, tokens)
                    if(tokens[next_token]['type'] == 'DOUBLE' or tokens[next_token]['type'] == 'INTEGER' 
                       or tokens[next_token]['type'] == 'CHAR'):
                        token_after_next = get_next_token(next_token,tokens)
                        if(tokens[token_after_next]['type'] == 'EOS'):
                            next_token = get_next_token(token_after_next, tokens)
                            if(tokens[next_token]['type'] == 'DEFINE'):
                                node. = data_declarations(next_token, tokens, node)
                            else:
                                current = next_token
                                return node
                        else:
                            print("SYNTAX ERROR") 
                            return None
                    else:
                        print("SYNTAX ERROR") 
                        return None
                else:
                    print("SYNTAX ERROR") 
                    return None            
            else:
                print("SYNTAX ERROR") 
                return None
    else:
        print("SYNTAX ERROR")
        return None
    
def begin(token, tokens, node):
    global current
    next_token = get_next_token(token, tokens)
    if(tokens[next_token]['value'] == 'EOS'):
        token_after_next = get_next_token(next_token,tokens)
        if(tokens[token_after_next]['value'] == 'DISPLAY'):
            next_token = get_next_token(token_after_next, tokens)
            if(tokens[next_token]['value'] == 'STRING'):
                token_after_next = get_next_token(next_token,tokens)
                if(tokens[token_after_next]['value'] == 'COMMA'):
                    next_token = get_next_token(token_after_next, tokens)
                    if(tokens[next_token]['value'] == 'IDENTIFIER'):

                elif(tokens[token_after_next]['value'] == 'EOS'):
                    next_token = get_next_token(token_after_next, tokens)
                    if(tokens[next_token]['value'] == 'DISPLAY' or
                       tokens[next_token]['value'] == 'SET' or
                       tokens[next_token]['value'] == 'EXIT'):
                        node. = begin(next_token, tokens, node)
                        if(node. == None):
                            break
                        else:
                            return node
                else:
                    print("SYNTAX ERROR")
                    return None
            else:
                print("SYNTAX ERROR")
                return None
        elif(tokens[token_after_next]['value'] == 'SET'):
            next_token = get_next_token(token_after_next, tokens)
            if(tokens[next_token]['value'] == 'IDENTIFIER'):
                token_after_next = get_next_token(next_token,tokens)
                if(tokens[token_after_next]['value'] == 'EQUALS'):
                    next_token = get_next_token(token_after_next, tokens)
                    if(tokens[next_token]['value'] == 'IDENTIFIER' or 
                       tokens[next_token]['value'] == 'num'):
                        node. = expressions(next_token, tokens, node)
                        if(node. == None):
                            break
                else:
                    print("SYNTAX ERROR")
                    return None
            else:
                print("SYNTAX ERROR")
                return None
        elif(tokens[token_after_next]['value'] == 'EXIT'):

        else:
            print("SYNTAX ERROR")
            return None

    else:
        print("SYNTAX ERROR")
        return None
    
def expressions(token, tokens, node):
    


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

    # for key, value in tokens.items():
        # print(f"Key: {key}, Value {value}")
        # print(value['value'])
        
    # for key, token in tokens.items():
        # print(f"Key: {key}, Token {token}")
        # print(token['value'])
        # for subkey, value in token.items():
        #    print(f"Subkey: {subkey}, Value {value}")

    # print(tokens['Token_1'])
    for token in tokens:
        next_token = get_next_token(token, tokens)
        print(next_token)
            
