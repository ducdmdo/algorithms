import logging

LOG_FORMAT = " %(message)s"
logging.basicConfig(filename="recursion_convert_string.log",
                    level = logging.DEBUG,
                    format= LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()


def convertString(inputString):
    #logger.info("Start the function")
    if inputString == "":
        #logger.debug("inputString position is lesser than 2")
        #logger.info("inputstring position {}".format(inputString))
        return inputString
    else:
        #logger.info(" Recursive loop: position %s and value %s ".format(inputString[len(inputString)-1], convertString(inputString[:len(inputString)-1])))
        return inputString[len(inputString)-1] + convertString(inputString[:len(inputString)-1])

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


def reverseString(s, left=0, right=0):
    if right == 0:
        right = len(s) - 1

    if left >= right:
        return

    temp = s[right]
    s[right] = s[left]
    s[left] = temp
    print (s)
    reverseString(s, left + 1, right - 1)

print (reverseString(["H","E","L","L","O"]))
#print (reverse("HELLO123"))
#print (convertString("HELLO"))