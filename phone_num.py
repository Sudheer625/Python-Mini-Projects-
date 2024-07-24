# py to track geo-location using mobile number

import phonenumbers as pn

from test_num import num      # test_num.py => num = "your_number"

from phonenumbers import geocoder

ch_num = pn.parse(num,"CH") # c means country , h means history 

print(geocoder.description_for_number(ch_num,"en")) # country name 


from phonenumbers import carrier

service_num = pn.parse(num,"RO")

print(carrier.name_for_number(service_num,"en"))    # service provider name 