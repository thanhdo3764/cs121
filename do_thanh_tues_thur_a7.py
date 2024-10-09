def logMessage(logFile, message):
    with open(logFile, 'a') as f: #Open LogFile in append mode
        f.write(message + '\n') #add message to end plus new line

def getLine(inputFile, lineNumber):
    counter = 1 #create line counter
    with open(inputFile, 'r') as f: #open inputFile in read mode
        for line in f: #for each line in the file
            if counter == lineNumber: #if it is the line number
                return line #return the line
            counter += 1 #add 1 to counter if nothing is returned
    return None #return None if nothing is returned yet

def writeCSV(outputFile, data):
    with open(outputFile, 'w') as f: #open the outputFile in write mode
        for line in data: #for each line in data
            for word in range(len(line)): #change each word in the list into a string
                line[word] = str(line[word])
            f.write(','.join(line) + '\n') #join words in line into a string plus new line

def main():
    #logMessage('test.txt', 'goodbye')
    #print(getLine('test.txt', 7))
    matrix = [['cs', 121], ['cs', 122], ['cs', 223]]
    writeCSV('out', matrix)


if __name__ == '__main__':
    main()