


### dictionary

book = {"chap1":10 ,"chap2":20 ,"chap3":30}
print(book)
# add new key-values
book["chap4"] = 40
book["chap5"] = 50
print("dictionary :",book)
#accessing values
print(book["chap1"])
print(book["chap2"])

# methods

# display keys
print(book.keys())

for key in book.keys():
    print(key)


for key in book:
    print(key)


# display values
print(book.values())

for value in book.values():
    print(value)


# display key-value pairs
for key,value in book.items():
    print(key,value)


# remove key value
book.pop("chap1")  # will remove chap1-10 from dictionary
print("After Removing the Keys", book)


book.popitem() # will remove last inserted key-value
print("after execting popitems", book)

# new dictionary
newbook = {"chap8":80,"chap9":90}
book.update(newbook)   # newbook is added to book
print(book)

book = {"chap1":10,"chap2":20}
newbook = {"chap3":30 ,"chap4":40}
finalbook = { **book, **newbook}
print(finalbook)




book = {"chap1":10,"chap2":20}
newbook = {"chap3":30 ,"chap4":40}
finalbook = { **book, **newbook}
print(finalbook)


str1 = "hello"
str2 = "python"
finalstr = str1 + str2

alist = [10,20,30]
blist = [30,40,50]
finalist = alist + blist

atup = (40,50,60)
btup = (60,70,80)
finaltup = atup + btup
print(finaltup)

