from Token import *
import sys
import json
import re

# Need to figure out how to get it to get the file from the command line (sys.argv argv[1] for filename)
# and have it search the SCL folder for it rather than just the COPLGroupProject folder
def tokenizefile (filename):
    with open(filename) as file:
        document = [] #Nested List of Lists
        comment=False

        for line in file:
            if ("description" or "/*") in line: #Checks if line is the start of a comment block
                comment=True
                continue

            if "*/" in line: #checks if the comment block ends
                comment = False
                continue

            if comment == True: #Otherwise, the current line is still a comment, thus it will be skipped
                continue

            if "//" in line: #Remove single line comment
                line = line[:line.find("//")] 

            currentLine= line.split() #Splits line by whitespace into a list

            if not currentLine: #Checks for empty line
                continue
            
            document.append(currentLine) #Adds list to nested list

        for line in document:
            print(line)
        return document

#tokenizefile('SCL/welcome.scl')

commandLine = sys.argv #What is inputted into the CLI

#Command Line should take the form: python scl_Scanner.py SCL/[SCL File]
#Ex: python Test/scl_scanner.py SCL/welcome.scl
#May need to move to the correct directory with the cd command on the CLI

tokenizefile("welcome.scl")
in_quotes = False
identifier_id = 3000
identifier_list = {}
#Function for categorizing tokens
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
    
    # Keep this for easy testing. Remove once done testing
    tokens_list = tokenizefile("welcome.scl")
    """ 
    This will be how we actually read the file remove this line and quotes and other test line when ready
    tokens_list = tokenizefile(commandLine[1])
    """
    categorized_list = []

    for token in tokens_list:
        for item in token:
            # current_token = token_catorizer(item)
            # print(current_token)
            new_token = token_catorizer(item)
            categorized_list.append(new_token)
            print("Token created: ", new_token.get_data())
        new_token = Token('EndOfStatement', 1000, 'EOS')
        print("Token created: ", new_token.get_data())
        categorized_list.append(new_token)

