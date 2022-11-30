import numpy as np

G = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(G)
print(G[0])
print(G[:,0])


array = np.array([[1,2], [3,4], [5,6]])
print(array)
array2 = np.append(array, [[G[0][0]],[G[1][0]],[G[2][0]]], axis = 1)
print(array2)
