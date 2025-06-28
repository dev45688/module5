try:
    file=open("sample.txt","r")
    reading_file=file.read()
    print("Reading file content:")
    print(reading_file)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
