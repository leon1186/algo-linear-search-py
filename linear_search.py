# linear_search.py

# CamelCase version used in first test
def linearSearch(target, list_to_search):
    for index, value in enumerate(list_to_search):
        if value == target:
            return index
    return None


# snake_case version (tests also call this name)
def linear_search(target, list_to_search):
    return linearSearch(target, list_to_search)


# return ALL matches (global search)
def linear_search_global(target, list_to_search):
    indices = []
    for index, value in enumerate(list_to_search):
        if value == target:
            indices.append(index)
    return indices
