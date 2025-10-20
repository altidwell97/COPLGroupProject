import os
import sys
import json
from scl_interpreter import scanner 




# def get_next_token(token):



commandLine = sys.argv #What is inputted into the CLI


if __name__ == "__main__":


    if len(commandLine) < 2:
        print("Usage: python scl_scanner.py <file.scl> [output.json]")
        sys.exit(1)

    src_path = "SCL/" + commandLine[1]
    out_path = commandLine[2] if len(
        commandLine) >= 3 else "tokens_output.json"

    if not os.path.exists(src_path):
        print(f"Error: file not found: {src_path}")
        sys.exit(1)

    scanner(str(src_path), str(out_path))

    with open('tokens_output.json', 'r') as file:
        data = json.load(file)

    print(data)