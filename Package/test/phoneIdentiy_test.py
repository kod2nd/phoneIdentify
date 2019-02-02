import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../src")))
from phoneIdentify import *


def test_removeDuplicates():
    assert removeDuplicates(['a', 'a']) == ['a']
    assert removeDuplicates(['b', 'a']) == ['b', 'a']

def test_removeSpacesDashes():
    assert removeSpacesDashes("hello abc") == "helloabc"
    assert removeSpacesDashes("hello-abc") == "helloabc"
    assert removeSpacesDashes(" hello-abc ") == "helloabc"

def test_formatPhoneNumber():
    assert formatPhoneNumber("1234") == "+1234"


def test_getPhoneNumbers():
    # Basic Singapore Phone Number
    assert getPhoneNumbers("+6581761924") == ["+6581761924"]
    # Word infront of number
    assert getPhoneNumbers("hello +6581761924") == ["+6581761924"]
    # Same Numbers
    assert getPhoneNumbers("+6581761924 +6581761924") == ["+6581761924"]
    # Word and no + in front
    assert getPhoneNumbers("hello 6581761924") == ["+6581761924"]
    # Word and numbers seperated by spaces
    assert getPhoneNumbers("hello 65 8176 1924") == ["+6581761924"]
    # Word and numbers seperated by dashes
    assert getPhoneNumbers("hello 65-81761-924") == ["+6581761924"]
    # No Phone number
    # assert getPhoneNumbers("hello $1,234") == []
