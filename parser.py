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
current = ''
error = False
def start(tokens, trees):
    token_keys = list(tokens.keys())
    more_tokens = True
    current_token = token_keys[current]
    current = token_keys[0]
    while(more_tokens):
        # if(tokens[token_keys[current]]['type'] == 'IMPORT'):
        if(tokens[current]['type'] == 'IMPORT'):
            imports_tree_nodes = imports(tokens[token_keys[current]], tokens)
            if(imports_tree_nodes == None):
                break
        # elif(tokens[token_keys[current]]['type'] == 'SPECIFICATIONS'):
        if(tokens[current]['type'] == 'SPECIFICATIONS'):
            specifications_tree_nodes = specifications(tokens[token_keys[current]], tokens)
            if(specifications_tree_nodes == None):
                break
        # elif(tokens[token_keys[current]]['type'] == 'IMPLEMENTATIONS'):
        if(tokens[current]['type'] == 'IMPLEMENTATIONS'):
            implementations_tree_nodes = implementations(tokens[token_keys[current]], tokens)
            if(implementations_tree_nodes == None):
                break
        else


def imports(token, tokens):
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
        error = True
        return None


def specifications(token,tokens, node):
    next_token = get_next_token(token,tokens)
        

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
            
