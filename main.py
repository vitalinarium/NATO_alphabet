import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
dict_al = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input('enter your name: ').upper()
    try:
        new_w = [dict_al[w] for w in word]
    except KeyError:
        print('sorry. only letters please')
        generate_phonetic()
    else:
        print(new_w)

generate_phonetic()