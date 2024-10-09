class Cipher(object):
    def __init__(self, inputString):
        self.inputString = inputString
        self.encodedString = ''
        self.decodedString = ''

    def __repr__(self):
        s = 'Original String: %s\nEncoded String: %s\nDecoded String: %s' \
                % (self.inputString, self.encodedString, self.decodedString)
        return s

    #range of lower case 97-122
    #range of capital case 65-90
    def addNLetters(self, letter, n):
        letterNum = ord(letter) #designates letter number
        inLowerCaseRange = letterNum in range(97, 123) #argument for if letter is in lower case alphabet
        inUpperCaseRange = letterNum in range(65, 91) #argument for if letter is in upper case alphabet
        #If adding n exceeds the end of the alphabet
        if (ord('z') - letterNum < n and inLowerCaseRange) or (ord('Z') - letterNum < n and inUpperCaseRange):
            letterNum = letterNum - 26 + n #letterNum goes backwards (26 minus n)
        elif inLowerCaseRange or inUpperCaseRange: #else if character is in alphabet and n doesn't exceed
            letterNum += n #add n to letterNum
        return chr(letterNum) #return character representation of letterNum

    def subtractNLetters(self, letter, n):
        letterNum = ord(letter) #designates letter number
        inLowerCaseRange = letterNum in range(97, 123) #argument for if letter is in lower case alphabet
        inUpperCaseRange = letterNum in range(65, 91) #argument for if letter is in upper case alphabet
        #If subtracting n precedes the beginning of the alphabet
        if (letterNum - ord('a') < n and inLowerCaseRange) or (letterNum - ord('A') < n and inUpperCaseRange):
            letterNum = letterNum + 26 - n #letterNum moves forwards (26 minus n)
        elif inLowerCaseRange or inUpperCaseRange: #else if character is in alphabet and n doesn't precede
            letterNum -= n #subtract n to letterNum
        return chr(letterNum) #return character representation of letterNum

    def encipher(self, n):
        self.encodedString = '' #sets encodedString to blank
        for s in self.inputString: #for each character in inputString
            self.encodedString += self.addNLetters(s, n) #apply Caesar cipher n times

    def decipherEasy(self, n):
        self.decodedString = '' #sets decodedString to blank
        for s in self.encodedString: #for each character in encodedString
            self.decodedString += self.subtractNLetters(s, n) #reverse Caesar cipher n times

def main():
    myEncoder = Cipher('Caesar cipher? I prefer Caesar salad.')
    myEncoder.encipher(25)
    myEncoder.decipherEasy(25)
    print(myEncoder)
if __name__ == '__main__':
    main()
