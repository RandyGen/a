from sklearn.datasets import load_iris
import numpy as np
import kcluster

iris = load_iris()
x1 = iris.data
x = x1.astype(np.float32).tolist()
y1 = iris.target
y = y1.flatten().astype(np.float32).tolist()

cl = kcluster(x, k=3)
print(cl)
