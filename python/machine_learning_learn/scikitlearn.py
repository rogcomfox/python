from sklearn import datasets
import sklearn.datasets as d
import numpy as np

reg_data = d.make_regression()
complex_reg_data = d.make_regression(1000, 10, 5, 2, 1.0)
