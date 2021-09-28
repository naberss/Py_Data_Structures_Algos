import matplotlib.pyplot as plt
import numpy

x = [-0.42, 1.34, 1.6, 2.65, 3.53, 4.48, 5.48, 6.21, 7.49, 8.14, 8.91, 10.1]
y = [1.58, 1.61, 2.04, 5.47, 9.8, 16.46, 25.34, 33.32, 49.7, 58.79, 71.26, 93.34]

x = numpy.array(x)
y = numpy.array(y)

plt.plot(x, y, 'o-')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
