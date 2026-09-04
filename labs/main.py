def word_lengths(words):
    lengths = {}
    if not words:
        return {}
    for word in words:
        lengths[word] = len(word)
    # TODO: loop through `words` and populate `lengths` with word -> length of word

    return lengths