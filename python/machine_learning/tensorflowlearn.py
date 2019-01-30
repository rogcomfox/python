import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashinon_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashinon_mnist.load_data()