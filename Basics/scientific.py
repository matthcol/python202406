import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(10.0, 3.5, 1_000_000)
print(data)
plt.hist(data, bins=100)
plt.show()
print('The End')
