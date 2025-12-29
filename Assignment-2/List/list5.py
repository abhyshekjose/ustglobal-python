def remove_duplicates(numbers):
    unique_list = []

    for item in numbers:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list
numbers = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(numbers)
print(result)