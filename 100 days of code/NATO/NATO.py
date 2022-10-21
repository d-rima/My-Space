import pandas

phrase = input("What phrase would you like to translate: ").upper()
broken_phrase  = [letter for letter in phrase]

data = pandas.read_csv("100 days of code/NATO/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

phonetic_list = [phonetic_dict[letter] for letter in broken_phrase]

print(phonetic_list)

