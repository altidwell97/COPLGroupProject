import sys
import json

with open('welcome.scl') as file:
    document = []
    comment=False

    for line in file:
        if ("description" or "Description") in line: #Checks if line is the start of a comment block
            comment=True
            continue

        if "*/" in line: #checks if the comment block ends
            comment = False
            continue

        if comment == True: #Otherwise, the current line is still a comment, thus it will be skipped
            continue

        if "//" in line: #Remove single comment
            line = line[:line.find("//")] 

        currentLine= line.split() #Splits line by whitespace into a list

        if not currentLine: #Checks for empty line
            continue
        
        document.append(currentLine) #Adds list to nested list

    for line in document:
        print(line)

