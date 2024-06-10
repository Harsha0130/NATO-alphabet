import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

phonetic_data = {row.letter: row.code for [index, row] in data.iterrows()}
# print(phonetic_data)

word = input("Enter thr word : ").upper()
output_list = [phonetic_data[letter] for letter in word]
print(output_list)
