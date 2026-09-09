def has_all_vowels(word):
    required = {"a", "e", "i", "o", "u"}
    word = word.lower()
    for vowel in required:
        if vowel not in word:
            return False
    return True
    # TODO: build a set of vowels actually found in `word`,
    # then check if it contains all of `required`
    pass