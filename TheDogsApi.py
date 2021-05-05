import requests
import json
dogs_apik = '100ae381-76de-48ed-8a6d-73c6e11af170'
# print(response.json()["name"])
response = requests.get("https://api.thedogapi.com/v1/breeds")
dogs_data = response.json()
#lists for filtering
dogs_list = []
unlisted_dogs = []
behaviors = set()
breeds = set()


### data filtering changes
def filter_breeds(data):
    """Filters Through dogs_data to take care of missing breed data
    empty strings (only one case) are labeled msc, and missing breed_group keys are
    reconcilled with msc.

    There are technically 7 breeds total with 8 & 9 being mixed and msc. (in a set so unordered really)
    """
    for dog in data:
        try:
            dog["breed_group"]
            if dog["breed_group"] == "":
                dog["breed_group"] = "Miscellaneous"
            breeds.add(dog["breed_group"])
        except KeyError:
            # print(dog["name"] + " DID NOT HAVE A BREED!")
            dog["breed_group"] = "Miscellaneous"
            breeds.add(dog["breed_group"])

filter_breeds(dogs_data)
### test to see if filter_breeds() works ###
# print("breeds")
# print(len(breeds))
# for x in breeds:
#     print(x)
# print(breeds)


#For figuring out what dogs have temperments missing
def filter_temperament(data):
    for dog in data:
        try:
            dog["temperament"]
            if dog["temperament"] == "":
                dog["temperament"] = "unknown"
            behaviors.add(dog["temperament"])
        except KeyError:
            # print(dog["name"] + " DID NOT HAVE A TEMPERAMENT__!")
            dog["temperament"] = "unknown"
            behaviors.add(dog["temperament"])

filter_temperament(dogs_data)
### test to see if filter_temperment() works ###
# print(len(behaviors))
# for x in dogs_data:
#     if x["temperament"] == "unknown":
#         print("true")
### data filtering changes

###old
#This is to display the dog names and also their temperament
# count = 1
# for x in response.json():
#     #print(count, "Dog's name: " + x["name"]) #Dog's name
#     while count < 6: #Only display 5 dogs (for testing)
#         print([count], x["name"] + "'s temperament: " + x["temperament"]) #Dog's temperament
#         count += 1    
    
#         """
#         try:
#             print(x["name"] + "'s temperament: " + x["temperament"]) #Dog's temperament
#         except KeyError:
#             print("DID NOT HAVE TEMPERAMENT") #If the dog doesn't have a temperament
#         count+=1
#         # print(x["life_span"])
#         # dog_list.append(x)
#         """


