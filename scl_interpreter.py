import os
from Token import *
import sys
import json
import re

# Need to figure out how to get it to get the file from the command line (sys.argv argv[1] for filename)
# and have it search the SCL folder for it rather than just the COPLGroupProject folder


def tokenizefile(filename):
    with open(filename) as file:
        document = []  # Nested List of Lists
        comment = False

        for line in file:
            # I fixed for original logic:
            # ("description" or "/*") in line is always True in Python.
            # Checks if line is the start of a comment block
            if ("description" in line) or ("/*" in line):
                comment = True
                continue

            if "*/" in line:  # checks if the comment block ends
                comment = False
                continue

            if comment == True:  # Otherwise, the current line is still a comment, thus it will be skipped
                continue

            if "//" in line:  # Remove single line comment
                line = line[:line.find("//")]

            currentLine = line.split()  # Splits line by whitespace into a list

            if not currentLine:  # Checks for empty line
                continue

            document.append(currentLine)  # Adds list to nested list
        return document

# tokenizefile('SCL/welcome.scl')


commandLine = sys.argv  # what is inputted into the CLI
in_quotes = False
identifier_id = 3000
identifier_list = {}
def token_catorizer(token):
    global in_quotes
    global identifier_id
    if in_quotes == True:
        if str(token).endswith("\"") or str(token).startswith("\""):
            set_boolean(False)
            return Token("StringLiteral", 5000, token)
        else:
            return Token("StringLiteral", 5000, token)
    else:
        if str(token).startswith("\"") and str(token).endswith("\""):
            return Token("StringLiteral", 5000, token)
        elif str(token).startswith("\""):
            set_boolean(True)
            return Token("StringLiteral", 5000, token)
        elif token in token_list["keywords"]:
            return Token("Keyword", token_list["keywords"][token], token)
        elif token in token_list["operators"]:
            return Token("Operator", token_list["operators"][token], token)
        elif token in token_list["special symbols"]:
            return Token("SpeacialSymbol", token_list["special symbols"][token], token)
        elif re.match(r"[a-zA-Z_]", str(token)):
            if token in identifier_list:
                return Token("Identifier", identifier_list[token], token)
            identifier_id += 1
            identifier = Token("Identifier", identifier_id, token)
            identifier_list[token] = identifier_id
            return identifier
        elif re.match(r"[0-9]", str(token)):
            return Token("NumericaLiteral", 4000, token)
        return Token("Unkown", 1200, token)

def set_boolean(new_value):
    global in_quotes
    in_quotes = new_value

#tokenizefile('SCL/welcome.scl')

commandLine = sys.argv #What is inputted into the CLI

#Command Line should take the form: python scl_Scanner.py SCL/[SCL File]
#Ex: python Test/scl_scanner.py SCL/welcome.scl
#May need to move to the correct directory with the cd command on the CLI
if __name__ == "__main__":
    if len(commandLine) < 2:
        print("Usage: python scl_scanner.py SCL/<file.scl> [output.json]")
        sys.exit(1)

    src_path = commandLine[1]
    out_path = commandLine[2] if len(
        commandLine) >= 3 else "tokens_output.json"

    if not os.path.exists(src_path):
        print(f"Error: file not found: {src_path}")
        sys.exit(1)

    # runs og tokenizer
    document = tokenizefile(src_path)

    categorized_list = []

    final_dictionary = {}

    for token in document:
        for item in token:
            # current_token = token_catorizer(item)
            # print(current_token)
            new_token = token_catorizer(item)
            categorized_list.append(new_token)
            print("Token created: ", new_token.get_data())
        new_token = Token('EndOfStatement', 1000, 'EOS')
        print("Token created: ", new_token.get_data())
        categorized_list.append(new_token)

    iterator = 0
    for Token in categorized_list:
        token_str = "Token_" + str(iterator)

        token_data = Token.get_data()
        token_dictionary = {
            "type": token_data[0],
            "id": token_data[1],
            "value": token_data[2]
        }

        final_dictionary[token_str] = token_dictionary
        iterator += 1


    #  write json showing both shapes
    payload = {
        "source": src_path,
        "tokens_by_line": document,
        "tokens_flat": final_dictionary
    }
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print(f"JSON written to: {out_path}")
