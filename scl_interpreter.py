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

        # print tokenized lines
        for line in document:
            print(line)

        return document

# tokenizefile('SCL/welcome.scl')


commandLine = sys.argv  # what is inputted into the CLI

# Command Line should take the form: python scl_Scanner.py SCL/[SCL File]
# Ex: python Test/scl_scanner.py SCL/welcome.scl
# May need to move to the correct directory with the cd command on the CLI

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

    # Build a flat list for token streaming
    flat_tokens = [tok for line in document for tok in line]

    # Print summary
    print(f"\nTotal lines tokenized: {len(document)}")
    print(f"Total tokens (flat): {len(flat_tokens)}")

    #  write json showing both shapes
    payload = {
        "source": src_path,
        "tokens_by_line": document,
        "tokens_flat": flat_tokens
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print(f"JSON written to: {out_path}")
