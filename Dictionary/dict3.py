marks = {"Math": 78, "Science": 45, "English": 67, "Physics": 49}
def keys_with_values_above_50(d):
    result = []

    for key, value in d.items():
        if value > 50:
            result.append(key)

    return result

print(keys_with_values_above_50(marks))
