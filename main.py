import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

phonetic_data = {row.letter: row.code for [index, row] in data.iterrows()}
print(phonetic_data)


def generate_phonetic():
    word = input("Enter the word : ").upper()
    try:
        output_list = [phonetic_data[letter] for letter in word]
    except KeyError:
        print("Sorry, Enter the letters only")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
