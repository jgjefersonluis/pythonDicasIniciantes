filename = 'siddhartha.txt'
with open(filename) as file_object:
    lines = file_object.readline()

for lines in lines:
    print(lines)