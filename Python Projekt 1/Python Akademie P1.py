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

oddelovac = "-" * 40

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
user = input("username: ")
password = input("password: ")

if users.get(user) != password:
    print("unregistered user, terminating the program..")

else:
    print(oddelovac)
    print(f"Welcome to the app, {user}\nWe have 3 texts to be analyzed.")
    print(oddelovac)

    input_textu = input("Enter a number btw. 1 and 3 to select:")

    if input_textu.isnumeric() is not True:
        print("Not available, terminating the program..")

    else:
        vyber_textu = int(input_textu)

        print(oddelovac)

        if vyber_textu < 1 or vyber_textu > 3:
            print("Not available, terminating the program..")

        elif type(vyber_textu) is not int:
            print("Not available, terminating the program..")

        else:
            words = []
            words_text = TEXTS[(vyber_textu) - 1]
            for slovo1 in words_text.split():
                words.append(
                    slovo1.strip(",.:;")
                )

            words_count = len(words)
            print("There are", words_count, "words in the selected text.")

            titlecase_words = []
            for slovo2 in words:
                if slovo2.istitle():
                    titlecase_words.append(slovo2)
                else:
                    continue

            titlecase_count = len(titlecase_words)
            print("There are", titlecase_count, "titlecase words.")

            uppercase_words = []
            for slovo3 in words:
                if slovo3.isupper() and slovo3.isalpha():
                    uppercase_words.append(slovo3)
                else:
                    continue

            uppercase_count = len(uppercase_words)
            print("There are", uppercase_count, "uppercase words.")

            lowercase_words = []
            for slovo4 in words:
                if slovo4.islower() and slovo4.isalpha():
                    lowercase_words.append(slovo4)
                else:
                    continue

            lowercase_count = len(lowercase_words)
            print("There are", lowercase_count, "lowercase words.")

            numeric_words = []
            for slovo5 in words:
                if slovo5.isnumeric():
                    numeric_words.append(slovo5)
                else:
                    continue

            numeric_count = len(numeric_words)
            print("There are", numeric_count, "numeric strings.")

            numbers = []
            for number in numeric_words:
                numbers.append(int(number))
            numbers_count = sum(numbers)
            print("The sum of all the numbers:", numbers_count)

            print(oddelovac)

            print("LEN|  OCCURENCES        |NR.")

            print(oddelovac)

            lenght = []
            counts = {}
            for slovo in words:
                lenght.append(len(slovo))
            for number in lenght:
                if number not in counts:
                    counts[number] = 1

                else:
                    counts[number] = counts[number] + 1
            for key, value in sorted(counts.items()):
                if key < 10:
                    print("", key,"|", "*" * value,(" " * (17 - value)),"|", value)
                else:
                    print(key, "|", "*" * value, (" " * (17 - value)), "|", value)










