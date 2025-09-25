import sys
import json

with open('welcome.scl') as file:
    document = []
    for line in file:


        currentLine= line.split()

        if not currentLine: #Checks for empty line
            continue
        
        document.append(currentLine)

    for line in document:
        print(line)

""""
#filter out comments    
    comment = False
    for line in document:
        for token in line:
            ##check if the token is a comment or has description
            if token == "description":
                comment=True
    if "*/" in line:
        comment = False
                
"""
#Maybe use boolean for status of comments such as if there is a comment