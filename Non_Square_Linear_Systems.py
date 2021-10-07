import numpy as np

x = np.array([[1,1,-1,-1],[2,-1,1,1],[3,1,2,2]])
y = np.array([-2,1,-1])

x = np.linalg.lstsq(x,y)

print(x)

