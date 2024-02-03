
#fd = open("C:\\Users\\IGS\\Desktop\\flag.txt", "r")
#file = open("C:\\Users\\IGS\\Desktop\\flag.txt", "r+")
file = open("C:\\Users\\IGS\\Desktop\\flag.txt", "w+")
# Read contents from file
contents = file.read()
print(contents)
print(file.tell())
# Read first 4 char only
#contents = file.read(4)

# Writing to files
contents = "success"
file.write(contents)

print(contents)
file.close()
# Close file after reading contents