import re as regex
from more_itertools import unique_everseen

mobileRegex = r'((\+[0-9]+\s*)?(\([0-9]+\))?([\s0-9\-]+[0-9]+))'


def removeDuplicates(lst):
    return list(unique_everseen(lst))


def removeSpaces(string):
    return string.replace(" ", "")


def formatPhoneNumber(phoneNumber):
    if phoneNumber[0] != "+":
        return "+" + phoneNumber
    return phoneNumber


def getMobileNumbers(text):
    mobileNumsRaw = [group[0] for group in regex.findall(mobileRegex, text)]

    mobileNumsProcessed = [removeSpaces(number) for number in mobileNumsRaw]

    mobileNumsFormatted = [formatPhoneNumber(
        number) for number in mobileNumsProcessed]

    return removeDuplicates(mobileNumsFormatted)
