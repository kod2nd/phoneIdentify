import re as regex
from more_itertools import unique_everseen

phoneRegex = r'((\+[0-9]+\s*)?(\([0-9]+\))?([\s0-9\-]+[0-9]+))'


def removeDuplicates(lst):
    return list(unique_everseen(lst))


def removeSpacesDashes(string):
    stringNoSpaces = string.replace(" ", "")
    stringNoDashes = stringNoSpaces.replace("-", "")
    return stringNoDashes


def formatPhoneNumber(phoneNumber):
    if phoneNumber[0] != "+":
        return "+" + phoneNumber
    return phoneNumber


def getPhoneNumbers(text):
    phoneNumsRaw = [group[0] for group in regex.findall(phoneRegex, text)]

    phoneNumsProcessed = [removeSpacesDashes(
        number) for number in phoneNumsRaw]

    phoneNumsFormatted = [formatPhoneNumber(
        number) for number in phoneNumsProcessed]

    return removeDuplicates(phoneNumsFormatted)
