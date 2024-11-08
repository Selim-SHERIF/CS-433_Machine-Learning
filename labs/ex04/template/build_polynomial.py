# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree.

    Args:
        x: numpy array of shape (N,), N is the number of samples.
        degree: integer.

    Returns:
        poly: numpy array of shape (N,d+1)

    >>> build_poly(np.array([0.0, 1.5]), 2)
    array([[1.  , 0.  , 0.  ],
           [1.  , 1.5 , 2.25]])
    """
    # ***************************************************
    N = x.shape[0]  # Number of data points
    poly = np.zeros((N, degree + 1))  # Create a 2D array with shape (N, degree + 1)
    
    for j in range(N):  # Iterate through all elements
        for i in range(degree + 1):  # Iterate through polynomial degrees
            poly[j, i] = x[j] ** i  # Access elements using square brackets
    
    return poly
        
    # ***************************************************