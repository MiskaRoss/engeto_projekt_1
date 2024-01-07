"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michaela Rossmannová
email: rossmannova.m@gmail.com
discord: misa02907
"""

delimiter = "-" * 40

registred_users = {"bob": "123", 
                    "ann": "pass123", 
                    "mike": "password123", 
                    "liz": "pass123"}


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Enter your username and password:
username = input("username: ")
password = input("password: ")

# Make sure your credentials are correct:
if username in registred_users and registred_users[username] == password:
    print(delimiter, sep="\n")
    print(f"Welcome to the app, {username} \nwe have {len(TEXTS)} texts to be analyzed.")
    print(delimiter, sep="\n")
elif username in registred_users and registred_users[username] != password:
    print("wrong password, terminating the program..")
    quit()
else:    
    print("unregistered user, terminating the program..")
    quit()

# Selecting text:
choice = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))
print(delimiter, sep="\n")

# Split text into words:
if choice >=1 and choice <= len(TEXTS):
    selected_text = TEXTS[choice - 1]
else:
    print("The selected number does not match the text.")
    quit()
      
# Convert words to a list:
clean_words = []
for word in selected_text.split():
    word = word.strip(" ,.:;'")
    clean_words.append(word.lower())

# Word count:
occurennce_of_words = {}   
for word in clean_words:
    if word not in occurennce_of_words:
        occurennce_of_words[word] = 1
    else:
        occurennce_of_words[word] += 1
sum_words = (sum(occurennce_of_words.values()))

# Word counting:
titlecase = 0
uppercase = 0
lowercase = 0
numeric_strings = 0

for word in selected_text.split():
    if word.istitle():      # Number of words starting with a capital letter
        titlecase += 1
    elif word.isupper():    # Number of words in capital letters
        uppercase += 1
    elif word.islower():    # Number of lowercase words
        lowercase +=1
    elif word.isnumeric():  # Number of numbers
        numeric_strings += 1
    else:
        pass

sum_numeric = []            # The sum of all numbers in the text.
for number in clean_words:
    if number.isnumeric():
        sum_numeric.append(int(number))

print(f"There are {sum_words} words in the selected text")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {numeric_strings} lowercase words.")
print(f"The sum of all the numbers {sum(sum_numeric)}.")

print(delimiter, sep="\n")
print("LEN|\t", "OCCURENCES\t", "|NR.")
print(delimiter, sep="\n")

#chart:
lenght_of_words = {}
for word in clean_words: 
    lenght = len(word)
    if lenght not in lenght_of_words:
        lenght_of_words[lenght] = 0
    lenght_of_words[lenght] += 1

for lenght in sorted(lenght_of_words):
    print(f'{lenght:3}| {"*" * lenght_of_words[lenght]:20}| {lenght_of_words[lenght]}')
