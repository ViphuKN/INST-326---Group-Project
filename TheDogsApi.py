import requests
# import json
import os
from pathlib import Path

#store data in response
response = requests.get("https://api.thedogapi.com/v1/breeds")
#format data to json
dogs_data = response.json()
#lists for all dog breeds, just name
dogs_list = []
#stores 9 breed types
breeds = set()
#stores all possible temperaments
behaviors = set()
# list of classes
dogs = []

#puts all dogs names in a global list
def store_dog_names(data):
    for dog in data:
        dogs_list.append(dog['name'])
#run after filer_temperament if needed but prolly won't need TBH just in case
# def store_behaviors(behaviors_list):
    # behaviors = list(behaviors_list)
    # behaviors = sorted(behaviors)
    # return behaviors
### data filtering changes START ###
def filter_breeds(data):
    """Filters Through dogs_data to take care of missing breed types data
    empty strings (only one case) are labeled msc, and missing breed_group keys are
    reconcilled with msc.

    There are technically 7 breeds total with 8 & 9 being mixed and msc. (in a set so unordered really)
    
    args:
        data - dog api jason data
    """
    for dog in data:
        #checks to see if breed types exists for each dog
        try:
            dog["breed_group"]
            if dog["breed_group"] == "":
                dog["breed_group"] = "Miscellaneous"
            breeds.add(dog["breed_group"])
        except KeyError:
            # print(dog["name"] + " DID NOT HAVE A BREED!")
            dog["breed_group"] = "Miscellaneous"
            breeds.add(dog["breed_group"])
#wrangles data, stores in set
def filter_temperament(data):
    """Puts all possible behaviors in a global set & makes dog temperment a list rather than a string. 
    If no temperment, then we place unkown into list as a place holder
    args:
        data - dog api jason data
    """
    for dog in data:
        try:
            #check for temperament values under temperament keys
            dog["temperament"]
            # if dog["temperament"] == "":
            #     dog["temperament"] = "unknown"
            dog["temperament"] = dog["temperament"].split(', ')
            for t in dog["temperament"]:
                behaviors.add(t)
        except KeyError:
            #if no temperament key, then create key with unknown value for pair
            dog["temperament"] = ["unknown"]
            for t in dog["temperament"]:
                behaviors.add(t)
#for wrangling heigth groups
def filter_heights(data):
    """Filters Through dogs_data to wrangle heights. Changes imperial key values into a
    list containing the dog heights range. If only one value in string, then we add 2 inches to height.
    If no height then we add 0 minimum 1 maximum as a place holder.

    args:
        data - dog api jason data
    """
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
    """Filters Through dogs_data to wrangle weights. Changes imperial key values into a
    list containing the dog weights range. If only one value in string, then we add 2 pounds to weight.
    If no weight then we add 0 minimum 1 maximum as a place holder.

    args:
        data - dog api jason data
    """
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
    """Filters Through dogs_data to wrangle life span. Changes key values into a
    list containing the dog age range. If only one value in string, then we add 2 years to range.
    If no age then we add 0 minimum 1 maximum to list as a place holder.

    args:
        data - dog api jason data
    """
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

            for year in years:
                year = int(year)
                life_span.append(year)
            if len(life_span) == 1:
                #if only one year for life span, we append year by += 2 for second year
                life_span.append(life_span[0] + 2)
            dog['life_span'] = life_span

        except KeyError:
            #dog height unknown so placeholder variables for years
            # print(dog["name"] + "has no LIFE SPAN")
            dog["life_span"] = [0,1]
#for wrangling photos
def get_photos(data):
    """Creates subdirectory 'dog_images' to store images from dogs_data. Made to only run once, it stores an image for each
    dog with the appropriate filename. accounts for jpg and png file types.
    args:
        data - dog api jason data
    """
    cwd = os.getcwd()
    p = Path('dog_images')
    p.mkdir(exist_ok=True)
    #change directory, needed to write photos to
    os.chdir('dog_images')
    #loop through data to create filenames corresponding to image data types
    for dog in data:
        try:
            url = dog['image']['url']
            name = dog['name']
            png_suffix = '.png'
            jpeg_suffix = '.jpg'
            #for jpg
            if url.endswith(jpeg_suffix):
                file_name = dog['name'] + ".jpg"
                dog[name] = file_name
                r = requests.get(url)
            #for png
            elif url.endswith(png_suffix):
                file_name = dog['name'] + ".png"
                dog[name] = file_name
                r = requests.get(url)
            #if image file exists start loop again   
            if os.path.exists(file_name):
                continue
            #if the image file doesn't exist we will write to directory
            with open(file_name, 'wb') as f:
                f.write(r.content)
        #error handling
        except KeyError:
            print("no URL!")
    #change directory back to parent directory
    os.chdir(cwd)
### data filtering changes END ###
#create classes
def create_classes(data):
    for dog in data:
        name = dog['name']
        breed_group = dog['breed_group']
        weight = dog['weight']['imperial']
        height = dog['height']['imperial']
        temperament = dog['temperament']
        filename = dog[name]
        dogs.append(Dog(name, breed_group, weight, height, temperament, filename))

    pass
#dog class
class Dog():
    """Used for every dog in JSON data
    """
    def __init__(self, name, breed_group, weight, height, temperament, filename):
        """creates an instnace of dog for ease of info retrival using specific data from JSON data
        args:
            name = string, represents dog name
            weight = list(len=2), represents weight as range
            height = list(len=2), represents height as range
            temperament = list of strings, ea. string is a temperament
            filename = string, a filename indicating the dogs corresponding photo
        """
        self.name = name
        self.breed_group = breed_group
        self.weight = weight
        self.height = height
        self.temperament = temperament
        self.filename = filename

def main(data):
    #modifies the dogs api json information
    filter_breeds(data)
    filter_temperament(data)
    filter_heights(data)
    filter_weights(data)
    filter_life_span(data)
    store_dog_names(data)
    get_photos(data)
    create_classes(data)


# main(dogs_data)

#run if need behaviors set() converted into a SORTED LIST
# behaviors = store_behaviors(behaviors)



