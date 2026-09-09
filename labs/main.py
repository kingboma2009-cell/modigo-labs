def dedupe_preserve_order(items):
    return list(dict.fromkeys(items))
    # TODO: use a set to track seen values while building a new list
    # that preserves the original order of first appearances
    pass