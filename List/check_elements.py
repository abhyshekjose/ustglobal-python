my_list = [10, 20, 30, 40, 50]

# Take multiple numbers separated by spaces
elements_to_check = list(map(int, input("Enter elements to check in the list: ").split()))

for element in elements_to_check:
    if element in my_list:
        print(f"{element} is present in the list.")
    else:
        print(f"{element} is not present in the list.")