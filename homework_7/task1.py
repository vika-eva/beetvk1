a = input().split()
dict = {key:a.count(key) for key in set(a)}
print(dict)


# or


text = input().split()
dict = {}
for i in text:
       dict[i] = text.count(i)
print(dict)







