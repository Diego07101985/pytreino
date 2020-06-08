s1 = set()

s1.add(3)
s1.add(2)
s1.add(1)
s1.add(3)
s1.discard(3)

s2 = set([])
s2.update("abracofree")
s3 = set([])
s3.update([1, 2, 3, 4], [4, 3, 4, 3, 5])
print(s2)
print(s3)
print(s1)


l1 = [12, 23, 123, 54, 34, 23, 11, 1, 11, 11, 22]
s1 = set(l1)
l1 = list(s1)


print(l1)
print(l1[-1])
