word = input("Enter word to search: ")

file = open("example.txt", "r")
for line_no, line in enumerate(file, start=1):
    if word in line:
        print(f"Word found at line {line_no}: {line.strip()}")
    else:
        print(f"word not found ")
file.close()