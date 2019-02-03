# Regex Identifiers
Using regex to identify phone numbers and credit card numbers in a string of text

## Usage
```Package/src/phoneIdentify.py```

```python
    from phoneIdentify import getPhoneNumbers

    text = "Some text containing Phone Numbers +65-1234-5678"

    getPhoneNumbers(text)

    # Result will be a list of phone numbers
```

```Package/src/creditCardValidation.py```
```python
    from creditCardValidation import isValidCreditCard

    text = "Some text containing credit card 4111111111111111"

    isValidCreditCard(text)

    # Result will be a list of credit cards objects.

    ```
    Credit Card {'issuer': 'mastercard', 'cardNumber': '5105105105105100', 'passedCheckSum': True}
    ```


```


## Environment
python 3.7

## Installation
```pip install requirements.txt```