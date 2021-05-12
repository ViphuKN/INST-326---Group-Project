import time
import requests
import json
import os
from pathlib import Path

dogs_apik = '100ae381-76de-48ed-8a6d-73c6e11af170'
# print(response.json()["name"])
response = requests.get("https://api.thedogapi.com/v1/breeds")
dogs_data = response.json()
#lists for filtering
dogs_list = []
breeds = set()
behaviors = set()
# heights = set()

def display_behaviors(behaviors):
    for behaveior in behaviors:
        print(behaveior)
### data filtering changes START ###
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
#For figuring out what dogs have temperments missing
def filter_temperament(data):
    for dog in data:
        try:
            dog["temperament"]
            # if dog["temperament"] == "":
            #     dog["temperament"] = "unknown"
            dog["temperament"] = dog["temperament"].split(', ')
            for t in dog["temperament"]:
                behaviors.add(t)
        except KeyError:
            dog["temperament"] = ["unknown"]
            for t in dog["temperament"]:
                behaviors.add(t)
#for wrangling heigth groups
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
#for wrangling weights data in imperial
def filter_weights(data):
    for dog in data:
        try:
            #dog dict for weight w/ imerial key has value pair == list(#, #) not string as defualt
            # metric is the same, a string
            weight = dog['weight']['imperial']
            if ' - ' in weight:
                weight = weight.split(" - ")
            elif ' – ' in weight:
                weight = weight.split(" – ")
            else:
                weight = [weight]
            if 'up' in weight:
                weight[0] = int(weight[1]) - 1
                weight[0] = str(weight[0])
                weight[1] = str(weight[1])
            #Changes string to interger
            new_weight = []
            for num in weight:
                num = float(num)
                new_weight.append(num)
            #formats height ranges missing 2nd value by adding 2" to 1st value for 2nd value
            if len(new_weight) == 1:
                new_weight.append(new_weight[0] + 2)
            dog['weight']['imperial'] = new_weight
        except KeyError:
            print("no weight")
            #dog height unknown so placeholder variables for imperial used
            dog["weight"]['imperial'] = [0, 1]
#for wrangling life span data
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
#for wrangling photos
def get_photos(data):
    # subdirectory = 'image_files'
    photos = {}
    cwd = os.getcwd()
    p = Path('dog_images')
    p.mkdir(exist_ok=True)
    os.chdir('dog_images')
    for dog in data:
        try:
            url = dog['image']['url']
            name = dog['name']
            png_suffix = '.png'
            jpeg_suffix = '.jpg'
            if url.endswith(jpeg_suffix):
                file_name = dog['name'] + ".jpg"
                photos[name] = file_name
                r = requests.get(url)
                # print(file_name)

            elif url.endswith(png_suffix):
                file_name = dog['name'] + ".png"
                photos[name] = file_name
                r = requests.get(url)
                # print(file_name)
            if os.path.exists(file_name):
                continue
            print("this executed")
            with open(file_name, 'wb') as f:
                f.write(r.content)
        except KeyError:
            print("no URL!")
    os.chdir(cwd)

### data filtering changes END ###
def main(data):
    #modifies the dogs api json informatio
    filter_breeds(dogs_data)
    filter_temperament(dogs_data)
    filter_heights(dogs_data)
    filter_weights(dogs_data)
    filter_life_span(dogs_data)
    get_photos(dogs_data)

main(dogs_data)





