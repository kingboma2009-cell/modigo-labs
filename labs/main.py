def list_average(numbers):
    if not numbers:
        return 0
    total = 0
    for p in numbers:
        total += p 
    return round(total / len(numbers), 2)
    # TODO: use a for loop to calculate the average of `numbers`, rounded to 2 decimal places
    pass