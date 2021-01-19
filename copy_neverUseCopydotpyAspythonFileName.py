import numpy as np

a=np.array([[1,2,3],[-4,-5,-6]])
print(np.sum(a[0,:]))
print(a)
print(abs(a))

print(np.sum(abs(a)))

b=np.arange(15).reshape(3,5)
print(b)

c=b  #복사 되지 않고 별명이 생김

c[0,0]=10 #수정시 b도 바뀜

print(c is b)

print(b)

#view copy
b=np.arange(21).reshape(3,7)
c=b.view()
c.shape=(1,21)

print(b)
print(c)
print(b is c)

