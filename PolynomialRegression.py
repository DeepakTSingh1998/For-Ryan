import numpy as np

## Compute Beta values
def Polynomial_Regression(x,y,order):
    X = np.zeros((len(x),order+1))
    for i in range(0,order+1):
        for j in range(0,len(x)):
            X[j,i] = pow(x[j],i)
            
    Beta = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X),X)),np.transpose(X)),y)
    return Beta, X
        
