import os
import sys
import json
from scl_interpreter import scanner 




def get_next_token(token, tokens):
    token_keys = list(tokens.keys())
    index_of_token = token_keys.index(token)
    if(index_of_token + 1 < len(token_keys)):
        return token_keys[index_of_token + 1]
    else:
        return None



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
            