import sys
import json

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

#tokenizefile('SCL/welcome.scl')

commandLine = sys.argv #What is inputted into the CLI

#Command Line should take the form: python scl_Scanner.py SCL/[SCL File]
#Ex: python Test/scl_scanner.py SCL/welcome.scl
#May need to move to the correct directory with the cd command on the CLI

tokenizefile(commandLine[1])

