def create_and_write_file():
    
    filename = "example.txt"
    
    try:  
        with open(filename, "w") as file:
            file.write("This is the first line.\n")
            file.write("Here is the second line.\n")
            file.write("And this is the third line.\n")
        
        print(f"File '{filename}' created and written successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

create_and_write_file()
