def squareOdds(x):
    l = [] #create empty list to return
    for n in x: #for every element in list x
        if n % 2 == 1: #if number is odd 
            l.append(n**2) #append n squared to l
    return l

def spaces(x):
    l = [' ' for space in x if space == ' '] #adds ' ' to list l for every space in string x
    return l

def specialChars(x):
    l = [] #create empty list to return
    for i in range(len(x)): #counts the element number in list x
        n = 0 #counts the characters in the elements
        for j in x[i]: #for every character in the current element
            if j == '$' or j == '!' or j == '@' or j == '&': #if there is a special character
                l.append(str(i)+str(n)) #add the strings of the element number and character number to l
            n += 1 #adds 1 to character counter for the subsequent character
    return l

def evenIndex(x):
    l = [] #create empty list to return
    for i in range(len(x)): #counts the element number in list x
        if i % 2 == 0 and x[i] % 2 == 0: #if the element number and the element itself is even
            l.append(i) #add the element number to l
    return l

def main():
    print(squareOdds([1,2,3,4]))
    print(spaces('how are you today'))
    print(specialChars(['he!!o', 'w@rld']))
    print(evenIndex([2, 4, 3, 3, 4, 5]))

if __name__ == '__main__':
    main()
