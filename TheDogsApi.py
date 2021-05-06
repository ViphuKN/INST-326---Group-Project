import requests
import json
dogs_apik = '100ae381-76de-48ed-8a6d-73c6e11af170'
# print(response.json()["name"])
response = requests.get("https://api.thedogapi.com/v1/breeds")
dogs_data = response.json()
#lists for filtering
dogs_list = []
unlisted_dogs = []
breeds = set()
behaviors = set()
heights = set()

# print(dogs_data[0])

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

#for identifying heigth/size groups
def filter_heights(data):
    for dog in data:
        try:
            #dog dict for height w/ imerial key has value pair == list(#, #) not string as defualt
            # metric is the same, a string
            height = dog['height']['imperial']
            height = height.split(" - ")
            new_height = []
            for num in height:
                num = float(num)
                new_height.append(num)
            #formats height ranges missing 2nd value by adding 2" to 1st value for 2nd value
            if len(new_height) == 1:
                new_height.append(new_height[0] + 2)
            dog['height']['imperial'] = new_height
        except KeyError:
            #dog height unknown so placeholder variables for imperial used
            dog["height"]['imperial'] = [0, 1]
            
#for identifying bred_for groups
def filter_life_span(data):
    # counter_y = 0
    # counter_n = 0
    for dog in data:
        try:
            life_span = []
            years = dog['life_span'].lower().replace(' years', '')
            if ' – ' in years:
                years = years.split(' – ')
            elif ' - ' in years:
                years = years.split(' - ')
            else:
                years = [years]
            # print(years)

            for year in years:
                year = int(year)
                life_span.append(year)
            if len(life_span) == 1:
                #if only one year for life span, we append year by += 2 for second year
                life_span.append(life_span[0] + 2)
            dog['life_span'] = life_span
            # print(dog['life_span'])

            # counter_y += 1
        except KeyError:
            #dog height unknown so placeholder variables for years
            # print(dog["name"] + "has no LIFE SPAN")
            dog["life_span"] = [0,1]

            # counter_n += 1
    # print(counter_y)
    # print(counter_n)


filter_life_span(dogs_data)
print(dogs_data[-1]['life_span'])

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


