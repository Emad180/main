"""function to match two strings regardless of characters order, 
case sensitivity, and white spaces"""

string = input('Enter string: ')
match = input('Enter match: ')

def matchString(string, match):
    stringLower = string.lower()
    matchLower = match.lower()
    stringLowerRemoved = ''.join(stringLower.split(' '))
    matchLowerRemoved = ''.join(matchLower.split(' '))
    stringList = [i for i in stringLowerRemoved]
    matchList = [j for j in matchLowerRemoved]
    if len(matchList) != len(stringList):
        return
    else:
        for char in matchList:
            if char in stringList:
                stringList.remove(char)
            else:
                return
        print(string)
    

# Start runing the function
if __name__ == '__main__':
    matchString(string, match)