# regular way # traditional way
fobj = open("customers.txt","w")
fobj.write("python\n")
fobj.write("unix\n")
fobj.writelines(["java","oracle\n"])
fobj.close()


# context manager
# if any lines starts using keyword with ... it is called context manager
# Advantage : file gets closed automatically

with open("customers.txt","w") as fobj:
    fobj.write("javascript\n")
    fobj.write("react JS\n")
    fobj.writelines(["java","oracle\n"])



# reading the file line by line
with open("customers.txt","r") as fobj:
    for line in fobj:
        print(line.strip())

# reading the file using fobj.readlines()
with open("customers.txt","r") as fobj:
    print(fobj.readlines())

# read the file using fobj.read()
with open("customers.txt","r") as fobj:
    print(fobj.read()) # single string

# using csv library
import csv
with open("customers.txt","r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)

# usingp pandas
import pandas as pd
df  = pd.read_csv("customers.txt",header = None)
print(df)