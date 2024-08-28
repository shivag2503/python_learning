import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


def define_phonetic():
    name = input("Enter the name: ").upper()
    try:
        result_2 = {item: new_dict[item] for item in name}
    except KeyError:
        print("Please enter alphabets only!!")
        define_phonetic()
    else:
        print(result_2)


define_phonetic()
