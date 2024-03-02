class PorterStemmer:
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.consonants = 'bcdfghjklmnpqrstvwxyz'
        self.step1a_suffixes = ["sses", "ies", "ss", "s"]
        self.step1b_suffixes = [("eed", "ee"), ("ed", ""), ("ing", "")]
        self.step2_suffixes = [
            ("ational", "ate"), ("tional", "tion"), ("enci", "ence"),
            ("anci", "ance"), ("izer", "ize"), ("abli", "able"),
            ("alli", "al"), ("entli", "ent"), ("eli", "e"),
            ("ousli", "ous"), ("ization", "ize"), ("ation", "ate"),
            ("ator", "ate"), ("alism", "al"), ("iveness", "ive"),
            ("fulness", "ful"), ("ousness", "ous"), ("aliti", "al"),
            ("iviti", "ive"), ("biliti", "ble")
        ]
        self.step3_suffixes = [
            ("icate", "ic"), ("ative", ""), ("alize", "al"),
            ("iciti", "ic"), ("ical", ""), ("ful", ""), ("ness", "")
        ]
        self.step4_suffixes = [
            ("al", ""), ("ance", ""), ("ence", ""), ("er", ""),
            ("ic", ""), ("able", ""), ("ible", ""), ("ant", ""),
            ("ement", ""), ("ment", ""), ("ent", "")
        ]
        self.step5a_suffixes = [("e", ""), ("e", "")]  # for some special cases
        self.step5b_suffixes = [("ll", "l")]

    def stem(self, word):
        if len(word) <= 2:
            return word  # Stemming is not applicable for short words
        word = self.step1a(word)
        word = self.step1b(word)
        word = self.step2(word)
        word = self.step3(word)
        word = self.step4(word)
        word = self.step5a(word)
        word = self.step5b(word)
        return word

    def step1a(self, word):
        for suffix in self.step1a_suffixes:
            if word.endswith(suffix):
                return word[:-len(suffix)]
        return word

    def step1b(self, word):
        for suffix, replacement in self.step1b_suffixes:
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.measure(stem) > 0:
                    return stem + replacement
                else:
                    return word
        return word

    def step2(self, word):
        for suffix, replacement in self.step2_suffixes:
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.measure(stem) > 0:
                    return stem + replacement
                else:
                    return word
        return word

    def step3(self, word):
        for suffix, replacement in self.step3_suffixes:
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.measure(stem) > 0:
                    return stem + replacement
                else:
                    return word
        return word

    def step4(self, word):
        for suffix, replacement in self.step4_suffixes:
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.measure(stem) > 1:
                    return stem + replacement
                else:
                    return word
        return word

    def step5a(self, word):
        for suffix, replacement in self.step5a_suffixes:
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.measure(stem) > 1:
                    return stem + replacement
                else:
                    return word
        return word

    def step5b(self, word):
        for suffix, replacement in self.step5b_suffixes:
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.measure(stem) > 1:
                    return stem + replacement
                else:
                    return word
        return word

    def measure(self, stem):
        """Returns the measure of a stem."""
        count = 0
        vowel_flag = False
        for char in stem:
            if char in self.vowels:
                if not vowel_flag:
                    count += 1
                    vowel_flag = True
            else:
                vowel_flag = False
        return count

# Example usage:
if __name__ == "__main__":
    stemmer = PorterStemmer()
    words = ["running", "flies", "cats", "trouble", "troubling", "troubled",
             "university", "universal", "universally", "probation", "singing", "complex", "complexity"]
    print("Original words:", words)
    stemmed_words = [stemmer.stem(word) for word in words]
    print("Stemmed words:", stemmed_words)
