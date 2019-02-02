import phonenumbers
from phonenumbers import PhoneNumberMatcher, geocoder
x = phonenumbers.parse("Hello my number is +65-9171 5067", None)
print(x)

y = phonenumbers.parse("020 8366 1177", "GB")
print(y)


text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."
numbers = []
for match in PhoneNumberMatcher(text, "US"):
    print(match.number)
    numbers.append("+1" + str(match.number.national_number))


print(numbers)
geolocation = geocoder.description_for_number(x, "en")
print(geolocation)
