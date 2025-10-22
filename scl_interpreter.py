import os
from Token import *
import sys
import json
import re

# Group: Alex Tidwell, Jennifer Morales, Sydney Forbes


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


identifier_id = 3000
identifier_list = {}
# Categorizes the type and creates a token object that contains the type, id,
# and value of a given token
def token_catorizer(token):
    global identifier_id
    # Checks for string contained within double quotes
    if str(token).startswith("\"") and str(token).endswith("\""):
        return Token("StringLiteral", 5000, token)
    # Searches Token.py for if the token matches a keyword
    elif token in token_list["keywords"]:
        return Token("Keyword", token_list["keywords"][token], token)
    # Searches Token.py for if the token matches an operator
    elif token in token_list["operators"]:
        return Token("Operator", token_list["operators"][token], token)
    # Searches Token.py for if the token matches a special symbol
    elif token in token_list["special symbols"]:
        return Token("SpeacialSymbol", token_list["special symbols"][token], token)
    # If token is not contained in Token.py and contains alphabetical characters
    # that are not within double quotes it becomes an identifier. Keeps track of 
    # previous identifiers so that multiple instances of one identifier are treated
    # as the same identifier
    elif re.match(r"[a-zA-Z_]", str(token)):
        if token in identifier_list:
            return Token("Identifier", identifier_list[token], token)
        identifier_id += 1
        identifier = Token("Identifier", identifier_id, token)
        identifier_list[token] = identifier_id
        return identifier
    # If token is not contained in Token.py and contains numeric characters
    # that are not within double quotes it becomes a numeric literal.
    elif re.match(r"[0-9]", str(token)):
        return Token("NumericaLiteral", 4000, token)
    # If token does not fall into any of the above categories
    return Token("Unknown", 1200, token)


#Command Line should take the form: python scl_Scanner.py SCL/[SCL File]
#Ex: python Test/scl_scanner.py SCL/welcome.scl
#May need to move to the correct directory with the cd command on the CLI
def scanner(src_path):
    in_quotes = False

    # runs tokenizer function
    document = tokenizefile(src_path)

    categorized_list = []

    final_dictionary = {}

    # Combine string literals within a set of double quotes into one token
    reorganized_document = []
    for line in document:
        line_of_doc = []
        for token in line:
            if in_quotes:
                if(token.endswith("\"")):
                    in_quotes = False
                    combined_token += (" " + token)
                    line_of_doc.append(combined_token)
                elif(token.startswith("\"")):
                    in_quotes = False
                    combined_token += " \""
                    line_of_doc.append(combined_token)
                    token = token[1:]
                    line_of_doc.append(token)
                else:
                    combined_token += (" " + token)
            else:
                if(token.startswith("\"") and not token.endswith("\"")):
                    in_quotes = True
                    combined_token = token
                    continue
                line_of_doc.append(token)
        reorganized_document.append(line_of_doc)

    # Runs through the list of list of the tokens and categorizes them by type
    for token in reorganized_document:
        for item in token:
            new_token = token_catorizer(item)
            categorized_list.append(new_token)
            print("Token created: ", new_token.get_data())
        new_token = Token('EndOfStatement', 1000, 'EOS')
        print("Token created: ", new_token.get_data())
        categorized_list.append(new_token)

    # Gives the categorized token objects a dictionary with string values
    iterator = 0
    token_dictionary = {}
    for token in categorized_list:
        token_str = "Token_" + str(iterator)
        token_data = token.get_data()
        token_dictionary[token_str] = {}
        token_dictionary[token_str] = {
            "type": str(token_data[0]),
            "id": str(token_data[1]),
            "value": str(token_data[2])
        }

        final_dictionary.update(token_dictionary)
        iterator += 1

    # Output the dictionary
    return final_dictionary

