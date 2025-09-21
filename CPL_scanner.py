'''
curString = (starting spot to end of line or whitespace)
if(curString matches a predefined keyword, like operator or whatever): Use that token value
Else: Check regular expresses, use whichever is longest, use that one

Do the above until the end of the string is reached

dict tokenDict [str --> int]
'''

tokenDict = {
    "main" : 0
}

import re
int curLine = 0
int tokenCounter = 0

def openFile(fileName):
    try:
        file = open(fileName, 'r')
        return file
    except Exception as e:
        print(e)
        exit(1)

def getNextNonEmptyLine(file):
    # Skip empty lines
    line = file.readline()
    while (re.match("^\s*$", line)):
        line = file.readLine()
    while (re.match("description", line)):
        while (not re.match("\*/")):
            line = file.readLine()

    return line

def regexCheck(lexeme):
    longestMatch = 0
    currentBestToken = "Unknown"





def processLine(curLine):
    curLexemeChunk = re.match("^\S+", curLine)
    startSlice = curLexemeChunk.len()
    curLine = curLine[startSlice:]
    returnArray = []

    while(curLine is not ""):
        while(curLexemeChunk is not ""):
            # Check if in tokenDict
            # Then check regex
            # If none, then mark as unknown
            # advance curLexeme pointer
            # do until curLexemeChunk consumed
            if curLexemeChunk in tokenDict:
                dictEntry = {
                    "Type" : "keywords",
                    "id": tokenDict[curLexemeChunk],
                    "Value" : curLexemeChunk
                }
                returnArray.append(dictEntry)
            else if :









fileName = input("Enter file name: ")
file = openFile(fileName)

curLine = getNextNonEmptyLine(file)

# while file still has more to process
while(curLine != ""):
    processLine(curLine)

    curLine = getNextNonEmptyLine(file)







