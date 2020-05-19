def sum_numbers(numbers = [x for x in range(1,101)]):
    try:
        total = sum(numbers)
    except TypeError:
        total = sum([x for x in range(1,101)])
    return total
