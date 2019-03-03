import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets, neighbors

#import some data to play with
iris = datasets.load_iris()

#we only take the first two features. We could avoid ugly slicing by using a two dim dataset
X = iris.data[:,:2]
Y = iris.target

