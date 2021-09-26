def removeWhite(s):
    return s.replace(" ","")

def isPal(inputString):
    inputString = inputString.replace(" ","")
    isMatched = True
    if len(inputString) <=1:
        return isMatched
    elif inputString[0] != inputString[len(inputString)-1]:
        return False
    else:
        return isPal(inputString[1:len(inputString)-1])

print (isPal("toot"))
#print (removeWhite("madam im adam"))