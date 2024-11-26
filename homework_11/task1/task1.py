file_one = open("myfile.txt", "a")
file_one.write("Hello file world!\n")
file_one.close()

file_two = open("myfile.txt", "r")
print(file_two.readlines())
file_two.close()