import numpy as np

# sistemas lineares devem ser resolvidos em pares no mínimo
x = np.array([[1,1,-1,-1],[2,-1,1,1],[3,1,2,2]])
y = np.array([-2,1,-1])

x = np.linalg.lstsq(x,y)

print(x)
# print(residuals)
# print(rank)
# print(s)

