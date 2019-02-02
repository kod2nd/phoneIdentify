import re as regex

cardRegex = {
    'visa': r'4[0-9]{12}(?:[0-9]{3})',
    'mastercard': r'(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}',
    'americanexpress': r'3[47][0-9]{13}',
    'dinersclub': r'3(?:0[0-5]|[68][0-9])[0-9]{11}',
    'discover': r'6(?:011|5[0-9]{2})[0-9]{12}',
    'jcb': r'(?:2131|1800|35\d{3})\d{11}'
}

def isValidCreditCard(creditCardNumber):
    creditCards = []
    for key in cardRegex.keys():
        for number in regex.finditer(cardRegex[key],creditCardNumber):
            creditCards = [*creditCards, number.group()]
    return creditCards
        

validcards = isValidCreditCard("4111111111111111. 4175002655356500 Person 2's card is: 5105105105105100 4222222222222222 32755514757031")
print(validcards)

