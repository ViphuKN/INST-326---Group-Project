import requests
import json
dogs_apik = '100ae381-76de-48ed-8a6d-73c6e11af170'
# print(response.json()["name"])
response = requests.get("https://api.thedogapi.com/v1/breeds")
# response1 = requests.get("https://api.thedogapi.com/v1/breeds/1")
# print(response.text)
# print(response.status_code)
# print(response.reason)
# print(response.headers)
# print(response.headers.get("Content-Type"))

# print(response.json())
# list_of_dogs = response.json()
# for dog in list_of_dogs:
#     print(dog)

# print(response1.json()["temperament"])
# print(response1.json())

dog_list = []
dog_behavior = []
set_db = set(dog_behavior)

for x in response.json():
    print(x["name"])
    try:
        print(x["temperament"])
    except KeyError:
        print("DID NOT HAVE TEMPERAMENT")
    # print(x["life_span"])
    # dog_list.append(x)

length = len(response.json())
num = 0

# while num <= length:
#     if response.json()[num]["temperament"]:
#         print(response.json()[num]["temperament"])
#     else:
#         print("none")
#     num+=1

# print(length)
# print(dog_list[0]["name"])
# print(dog_list[0]["temperament"])

