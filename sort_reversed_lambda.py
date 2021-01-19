list=[4,3,1,2,5,5]

list.sort()
print(list)

list2=[4,3,1,2,5,5]
list2=sorted(list2)
print(list2)

list2.sort(reverse=True)
print(list2)


dict_to_sort=[(1,5),(4,5),(2,7)]
print(dict_to_sort)
# sort후에 최대 값을 가져옴
sorted_dict=sorted(dict_to_sort,key=lambda x:x[0], reverse=True)

print(sorted_dict)
