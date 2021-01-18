
import numpy as np
import matplotlib.pyplot as plt
a=[1,2,3,4,5,6]
np.random.seed(42)
selection=[]
for i in range(10000):
    selection.append(a[np.random.randint(len(a))])

plt.hist(selection,6)
plt.show()

