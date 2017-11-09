a = set([5,4,8,5])
b = {5,3,8,5}
print(a)
print(5 in a)
a.add(2)
a.remove(4)
print(a)
print(len(a))


c= {1,3,5,8}
d={3,5,8,9}
print(c  | d)
print(c & d)
print(c - d)
