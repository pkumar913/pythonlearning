# set venn diagram

aset = {10, 20, 30, 40, 50, 60}
print(aset)


bset = {30, 40, 50, 60, 70}
print(bset)


print("Union :", aset.union(bset))
print("Intersection :", aset.intersection(bset))
print("differerence :", aset.difference(bset))

aset.add(10)
print(aset)
aset.add(40)
print(aset)