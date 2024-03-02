import string

def is_consonant(char):
    return char.lower() not in 'aeiou'

def get_measure(word):
    word = word.lower()
    count = 0
    index = 0
    while index < len(word):
        while index < len(word) and not is_consonant(word[index]):
            index += 1
        if index < len(word):
            count += 1
            index += 1
        while index < len(word) and is_consonant(word[index]):
            index += 1
    return count

def ends_double_consonant(word):
    if len(word) >= 2:
        if word[-1] == word[-2] and is_consonant(word[-1]):
            return True
    return False

def ends_cvc(word):
    if len(word) >= 3:
        if is_consonant(word[-3]) and not is_consonant(word[-2]) and is_consonant(word[-1]):
            if word[-1] not in 'wxY':
                return True
    return False

def replace_suffix(word, suffix, replacement):
    if word.endswith(suffix):
        return word[:-len(suffix)] + replacement
    return word

def porter_stemmer(word):
    if word.endswith('sses'):
        word = replace_suffix(word, 'sses', 'ss')
    elif word.endswith('ies'):
        word = replace_suffix(word, 'ies', 'i')
    elif word.endswith('ss'):
        pass
    elif word.endswith('s'):
        word = replace_suffix(word, 's', '')

    if word.endswith('eed'):
        if get_measure(word[:-3]) > 0:
            word = word[:-1]
    elif word.endswith('ed'):
        if 'v' in word[:-2]:
            word = word[:-2]
            if word.endswith('at') or word.endswith('bl') or word.endswith('iz'):
                word += 'e'
            elif ends_double_consonant(word) and word[-1] not in 'lsz':
                word = word[:-1]
            elif get_measure(word) == 1 and ends_cvc(word):
                word += 'e'
    elif word.endswith('ing'):
        if 'v' in word[:-3]:
            word = word[:-3]
            if ends_cvc(word):
                word += 'e'

    if word.endswith('y'):
        if get_measure(word[:-1]) > 0:
            word = word[:-1] + 'i'

    if word.endswith('ational'):
        if get_measure(word[:-7]) > 0:
            word = word[:-7] + 'ate'
    elif word.endswith('tional'):
        if get_measure(word[:-6]) > 0:
            word = word[:-6] + 'tion'
    elif word.endswith('enci'):
        if get_measure(word[:-4]) > 0:
            word = word[:-4] + 'ence'
    elif word.endswith('anci'):
        if get_measure(word[:-4]) > 0:
            word = word[:-4] + 'ance'
    elif word.endswith('izer'):
        if get_measure(word[:-4]) > 0:
            word = word[:-4] + 'ize'
    elif word.endswith('abli'):
        if get_measure(word[:-4]) > 0:
            word = word[:-4] + 'able'
    elif word.endswith('alli'):
        if get_measure(word[:-4]) > 0:
            word = word[:-4] + 'al'
    elif word.endswith('entli'):
        if get_measure(word[:-5]) > 0:
            word = word[:-5] + 'ent'
    elif word.endswith('eli'):
        if get_measure(word[:-3]) > 0:
            word = word[:-3] + 'e'
    elif word.endswith('ousli'):
        if get_measure(word[:-5]) > 0:
            word = word[:-5] + 'ous'
    elif word.endswith('ization'):
        if get_measure(word[:-7]) > 0:
            word = word[:-7] + 'ize'
    elif word.endswith('ation'):
        if get_measure(word[:-5]) > 0:
            word = word[:-5] + 'ate'
    elif word.endswith('ator'):
        if get_measure(word[:-4]) > 0:
            word = word[:-4] + 'ate'
    elif word.endswith('alism'):
        if get_measure(word[:-5]) > 0:
            word = word[:-5] + 'al'
    elif word.endswith('iveness'):
        if get_measure(word[:-7]) > 0:
            word = word[:-7] + 'ive'
    elif word.endswith('fulness'):
        if get_measure(word[:-7]) > 0:
            word = word[:-7] + 'ful'
    elif word.endswith('ousness'):
        if get_measure(word[:-7]) > 0:
            word = word[:-7] + 'ous'
    elif word.endswith('aliti'):
        if get_measure(word[:-5]) > 0:
            word = word[:-5] + 'al'
    elif word.endswith('iviti'):
        if get_measure(word[:-5]) > 0:
            word = word[:-5] + 'ive'
    elif word.endswith('biliti'):
        if get_measure(word[:-6]) > 0:
            word = word[:-6] + 'ble'

    if word.endswith('icate'):
        if get_measure(word[:-5]) > 0:
            word = word[:-5] + 'ic'
    elif word.endswith('ative'):
        if get_measure(word[:-5]) > 0:
            word = word[:-5]
    elif word.endswith('alize'):
        if get_measure(word[:-5]) > 0:
            word = word[:-5] + 'al'
    elif word.endswith('iciti'):
        if get_measure(word[:-5]) > 0:
            word = word[:-5] + 'ic'
    elif word.endswith('ical'):
        if get_measure(word[:-4]) > 0:
            word = word[:-4] + 'ic'
    elif word.endswith('ful'):
        if get_measure(word[:-3]) > 0:
            word = word[:-3]
    elif word.endswith('ness'):
        if get_measure(word[:-4]) > 0:
            word = word[:-4]

    if word.endswith('al'):
        if get_measure(word[:-2]) > 1:
            word = word[:-2]
    elif word.endswith('ance'):
        if get_measure(word[:-4]) > 1:
            word = word[:-4]
    elif word.endswith('ence'):
        if get_measure(word[:-4]) > 1:
            word = word[:-4]
    elif word.endswith('er'):
        if get_measure(word[:-2]) > 1:
            word = word[:-2]
    elif word.endswith('ic'):
        if get_measure(word[:-2]) > 1:
            word = word[:-2]
    elif word.endswith('able'):
        if get_measure(word[:-4]) > 1:
            word = word[:-4]
    elif word.endswith('ible'):
        if get_measure(word[:-4]) > 1:
            word = word[:-4]
    elif word.endswith('ant'):
        if get_measure(word[:-3]) > 1:
            word = word[:-3]
    elif word.endswith('ement'):
        if get_measure(word[:-5]) > 1:
            word = word[:-5]
    elif word.endswith('ment'):
        if get_measure(word[:-4]) > 1:
            word = word[:-4]
    elif word.endswith('ent'):
        if get_measure(word[:-3]) > 1:
            word = word[:-3]
    elif word.endswith('ism'):
        if get_measure(word[:-3]) > 1:
            word = word[:-3]
    elif word.endswith('ate'):
        if get_measure(word[:-3]) > 1:
            word = word[:-3]
    elif word.endswith('iti'):
        if get_measure(word[:-3]) > 1:
            word = word[:-3]
    elif word.endswith('ous'):
        if get_measure(word[:-3]) > 1:
            word = word[:-3]
    elif word.endswith('ive'):
        if get_measure(word[:-3]) > 1:
            word = word[:-3]
    elif word.endswith('ize'):
        if get_measure(word[:-3]) > 1:
            word = word[:-3]
    if word.endswith('e'):
        if get_measure(word[:-1]) > 1:
            word = word[:-1]
        elif get_measure(word[:-1]) == 1 and not ends_cvc(word[:-1]):
            word = word[:-1]

    if get_measure(word) > 1 and ends_double_consonant(word) and word.endswith('l'):
        word = word[:-1]

    return word
def main():
    words = [
        "caresses", "flies", "dies", "mules", "denied", "died", "agreed"
    ]


    print("{:15} {:15}".format("Word", "Stemmed"))
    print("-" * 30)
    for word in words:
        stemmed_word = porter_stemmer(word)
        print("{:15} {:15}".format(word, stemmed_word))

if __name__ == "__main__":
    main()
