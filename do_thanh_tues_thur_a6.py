def backupFile(inputFile, outputFile):
    with open(outputFile + '.bak', 'w') as oFile: #open file with name outputFile.bak to write
        with open(inputFile, 'r') as iFile: #open file with name inputFile to read
            oFile.write(iFile.read()) #writes inputFile copy into outputFile.bak

def addSemester(inputFile, outputFile):
    with open(outputFile, 'w') as oFile: #open file with name outputFile to write
        with open(inputFile, 'r') as iFile: #open file with name inputFIle to read
            for line in iFile: #for each line in inputFile
                line = line.strip()
                if line == 'cs 121' or line == 'cs 215' or line == 'cs 223' or line == 'cs 260':
                    line = line + ' fall' #if line is one of these courses, add fall
                if line == 'cs 122' or line == 'cs 166' or line == 'cs 224' or line == 'cs 251' or line == 'cs 261':
                    line = line + ' spring' #if line is one of these courses, add spring
                oFile.write(line + '\n') #writes the class and semester plus new line

def reverseLine(inputFile, outputFile):
    with open(outputFile, 'w') as oFile: #open file with name outputFile to write
        with open(inputFile, 'r') as iFile: #open file with name inputFile to read
            for line in iFile: #for each line in inputFile
                l = line.split() #separates words from line into a list
                for j in range(len(l)//2): #counts half of the words in the line to be flipped
                    opposite = l[-1*(j+1)] #saves the opposite word
                    l[-1*(j+1)] = l[j] #replaces opposite word with word j
                    l[j] = opposite #replaces word j with its opposite
                if '\n' in line: #If there is a new line in line, and new line
                    oFile.write(' '.join(l) + '\n')
                else: #if not, don't add new line
                    oFile.write(' '.join(l))

def storeTabDelimitedFile(inputFile):
    with open(inputFile, 'r') as f: #open file with name inputFile to read
        matrix = [] #separates lines into list elements
        for row in f: #for each line in f
            matrix.append(row.split('\t')) #create list of strings that were separated by tabs and appended to matrix
    return matrix44

def main():
    #backupFile('in.txt', 'out')
    #addSemester('in.txt', 'out')
    reverseLine('in.txt', 'out')
    #print(storeTabDelimitedFile('in.txt'))

if __name__ == '__main__':
    main()
