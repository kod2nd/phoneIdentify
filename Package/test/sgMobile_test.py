import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../src")))
from sgMobile import *


def test_removeDuplicates():
    assert removeDuplicates(['a', 'a']) == ['a']
    assert removeDuplicates(['b', 'a']) == ['b', 'a']


def test_joinedNumber():
    # Basic Singapore Mobile Number
    assert getMobileNumbers("+6581761924") == ["+6581761924"]
    # Word infront of number
    assert getMobileNumbers("hello +6581761924") == ["+6581761924"]
    # Same Numbers
    assert getMobileNumbers("+6581761924 +6581761924") == ["+6581761924"]
    # Word and no + in front
    assert getMobileNumbers("hello 6581761924") == ["+6581761924"]
    # Word and numbers seperated by spaces
    assert getMobileNumbers("hello 65 8176 1924") == ["+6581761924"]