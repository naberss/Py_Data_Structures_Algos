import numpy as np


x = np.array([[1,1],[2,4]])
y = np.array([35,94])

z,w = np.linalg.solve(x,y)

print(z)
print(w)
