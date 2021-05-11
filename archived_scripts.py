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

            # interger_map = map(int, height)
            # height = list(interger_map)
            # print(new_height)

### test to see if filter_breeds() works ###
# print("breeds")
# print(len(breeds))
# for x in breeds:
#     print(x)
# print(breeds)

### test to see if filter temperament() works ###
# print(behaviors)
# if 'unknown' in behaviors:
#     print('true')
# for dog in dogs_data:
#     print(dog["temperament"])

### V
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
