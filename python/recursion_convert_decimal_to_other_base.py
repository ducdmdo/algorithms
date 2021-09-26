def convertToOtherBase(inputNumber, base):
    convertString = "0123456789ABCDEF"
    if inputNumber < base:
        return convertString[inputNumber]
    else:
        return convertString[inputNumber%base] + convertToOtherBase(inputNumber//base,base)

print (convertToOtherBase(10,2))

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(10,2))
