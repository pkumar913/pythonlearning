##### list




alist = [67,34,67,4,82,56,64,23]

alist.append(100)
print("After appending:",alist)

alist.extend([56,32,5])
print("After extending :", alist)
#list.insert(index,value)
alist.insert(1,29)  
print("After inserting:",alist)
#list.pop(index)
alist.pop(3)
print("After pop operation:",alist)
#list.remove(value)
alist.remove(100)   # will work if the value is existing only
print("AFter remove operation :",alist)

if 1000 in alist:
    print("removed")
else:
    print("value not found")


# actual list will be updated
alist.sort()
print("sorting in ascending order:",alist)
alist.sort(reverse=True)
print("sorting in reverse order:",alist)
alist.reverse()
print("reversing list values :", alist)


# iterate the list
alist = [67,34,67,4,82,56,64,23]
for var in alist:
    print(var, sep = " ", end = "|")
