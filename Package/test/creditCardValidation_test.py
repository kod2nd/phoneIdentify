import os, sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../src")))
from creditCardValidation import *


def test_isValidCreditCard():
    # Check Sum
    assert isValidCreditCard('4111111111111111')[0]["passedCheckSum"] == True
    assert isValidCreditCard('Some text in front 4111111111111111')[0]["passedCheckSum"] == True
    assert isValidCreditCard('4175002655356500')[0]["passedCheckSum"] == False
    # Number Extraction
    assert isValidCreditCard('Some text in front 4111111111111111 some text behind')[0]["cardNumber"] == '4111111111111111'
    # Test against other numbers
    assert isValidCreditCard('Singapore Phone number 6591231234') == []
