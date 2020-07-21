from sys import argv

script, filename = argv


print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C") #If users does this since we dnt have a anything defined it will give error
print("If you do want that hit RETURN.")

input("? ")

print("Opening file...")
target = open(filename,'w') #write

print("Truncating the file. Goodbye!")
target.truncate() # Erase all contents of the file

print("Now lets insert 3 lines.")

l1 = input("Line 1: ")
l2 = input("Line 2: ")
l3 = input("Line 3: ")

print("Writing those line on the file...")

target.write(l1)
target.write("\n")
target.write(l2)
target.write("\n")
target.write(l3)
target.write("\n")

target.write(f"In a single line {l1} {l2} {l3}.")

print("Closing it.")
target.close() #Good practice, even without close the python will save the contents of the file

#If the file doesn't exist and you enter a random file name, python will create that file for you.