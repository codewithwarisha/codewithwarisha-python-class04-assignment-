# Writing to a file
with open("example.txt", "w") as file:
    file.write("This is a test file.\nLine 2.")

# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
