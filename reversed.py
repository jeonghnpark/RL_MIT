
li=[1,2,3,4,5]
type(li)
print(li)
for e in li:
    print(e)

re_li=reversed(li)
type(re_li)
# print(list(re_li))
# print(list(re_li))

print("print list(re_li)")
for re in list(re_li):
    print(re)

# reversed_list_range=reversed(range(9))
a=reversed(range(10))
a

print("a")
for i in a:
    print(i)


for i in reversed(range(10)):
    print(i)

a=range(10)
len(a)
for i in reversed(range(len(a)-1)):
    print(i)