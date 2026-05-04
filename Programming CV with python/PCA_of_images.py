from PIL import Image
from numpy import *

def pca(X):
    """Principal Component Analysis
        input: X, matrix with training data stored as flattend arrays in rows.
        return: Projection matrix ()
    """

    num_data, dim = X.shape