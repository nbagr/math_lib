from functools import reduce


def max(collection):
    max_element = collection[0]
    for item in collection[1:]:
        if item > max_element:
            max_element = item
    return max_element


def min(collection):
    min_element = collection[0]
    for item in collection[1:]:
        if item > min_element:
            min_element = item
    return min_element


def average(collection):
    return reduce(lambda acc, item: acc + item, collection, 0) / len(collection)


def sort(collection):
    steps_count = len(collection) - 1
    swapped = True

    while swapped:
        swapped = False
        for i in range(steps_count):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
                swapped = True
        steps_count -= 1

    return collection