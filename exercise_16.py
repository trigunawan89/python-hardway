from sys import argv

script, filename  = argv

print(f"we're going to erase {filename}")
print("If you don't wan that, hit CTRL-C (^C).")
print("If you want that hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,"w")

print("Truncating the file. Goodbye!")
target.truncate()


print("Now I'm going to ask you for three line.")

line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finnaly, we close it.")
target.close()

