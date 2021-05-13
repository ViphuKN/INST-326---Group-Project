# INST-326---Group-Project Gerson Roldan, Viphu Nguyen Elizabeth Arndt, Peter Chen
*Must have connection to the internet*
This program aids people in finding dogs that are right for them. The user inputs into the command line the type of dog breed that they are interested in learning more about. The program returns a neatly formatted list of dogs and their corresponding attributes that can be used by the user in order to help them make a decision about what specific dog breed they're interested in.

EXECUTABLE FILE: TheDogsApi.py

TO RUN IT: you should run the file from your terminal and enter: ```Python TheDogsApi.py __arg1__ __--arg2(optional)__```
arg 1) is a positional argument, there are 9 dog types that you are able to choose to learn more about from:
*'Herding', 'Miscellaneous', 'Toy', 'Terrier', 'Working', 'Non-Sporting', 'Sporting', 'Mixed', 'Hound'*
Choose one of the above.

arg 2) is an optional argument. There are two choices for this argument: 'yes flood' & 'no flood'
If left empty, it will default to 'no flood'.
if '--flood_photos "yes flood"' typed after arg 1 then you fill be flooded with photos from all the dog breeds listed under that breed type.

Once you've exectued your command line argument(s) and wait a few seconds, it will then reveal all the dog breeds in that breed category and display infomration in the following order: NAME/ Temerament/ Life Span/ Weight/ and Height.
If you opted to ' --flood_photos "yes flood" ' then all the photos corresponding to that breed type will open. While the filenames are correct, I'm not sure why the image doesn't open with correct filename.

*EXAMPLE COMMAND LINE EXAMPLES:*
- Python TheDogsApi.py "Toy" --flood_photos "yes flood"
- Python TheDogsApi.py "Toy" --flood_photos "no flood"

- Python TheDogsApi.py "Herding"
- Python TheDogsApi.py "Working"

# Bibliography:
```The Dog API:``` https://www.thedogapi.com/
Used to retrieve pictures of dog breeds and information about them.
