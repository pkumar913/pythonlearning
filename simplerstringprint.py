# string[start:stop:step]
name = "python programming"
print(name[0:18:2])
print(name[::1])
print(name[::])
print(name[:])
print(name[::-1])


print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.replace("python","scala"))
print(name.find("gra"))
print(name.find("abc"))  # if not found returns -1
print(name.isupper())
print(name.islower())
print(name.isalnum())
print(name.split(" "))
print(name.count("p"))

if name.isupper():
    print("this is upper case")
else:
    print("this is lower case")


# itereate the string
for val in range(1, 10):
    print(val)

for val in range(10, 1, -1):
    print(val)

name = 'python'
for char in name:
    print(char)

for char in name[::-1]:
    print(char)