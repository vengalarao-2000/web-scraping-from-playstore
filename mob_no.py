import phonenumbers
from track_no import number

from phonenumbers import geocoder

country = phonenumbers.parse(number)
print(geocoder.description_for_number(country,"en"))

from phonenumbers import carrier
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider,"en"))

# geocoder for identifying locationa and carrier for identifying service
#provider.


