# -*- coding: utf-8 -*-

import numpy as np


def relu(x):
	return np.maximum(x, 0)


def sigmoid(x):
	return 1 / (1 + np.exp(-x))
