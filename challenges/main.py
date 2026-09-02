def second_largest(numbers):
    # TODO: return the second largest DISTINCT number in `numbers`
    pass
    unique_number = list(set(numbers))
    unique_number.sort(reverse=True)
    return unique_number[1]