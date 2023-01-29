from __future__ import print_function
import warnings
warnings.filterwarnings('ignore')

import os
import numpy as np
from functools import partial
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.lay