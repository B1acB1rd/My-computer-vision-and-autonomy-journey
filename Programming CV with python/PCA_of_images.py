from PIL import Image
from numpy import *

def pca(X):
    """Principal Component Analysis
        input: X, matrix with training data stored as flattend arrays in rows.
        return: Projection matrix ()
    """
    #
    num_data, dim = X.shape
    #Center the data
    mean_X = X.mean(axis = 0)
    X = X - mean_X

    if dim > num_data:
        #PCA - compact trick used
        M = dot(X, X.T)
        e, EV = linalg.eigh(M)#This is for computing the eigen vectors and value sof a matrix
        tmp = dot(X.T, EV).T
        V = tmp[::-1] #Reverse since last eigen vectors are the one we want
        S = sqrt(e)[::-1]

        for i in range(V.shape[1]):
            V[:, i] /= S
        

    else:
        #PCS - SVD used
        U, S, V = linalg.svd(X)
        V = V[:num_data]

    return V, S, mean_X

