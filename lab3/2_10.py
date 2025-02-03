def unique_list(list):
    unique = []
    for item in list:
        if item not in unique:
            unique.append(item)
    return unique

print(unique_list([1, 2, 2, 3, 4, 4, 5])) 

