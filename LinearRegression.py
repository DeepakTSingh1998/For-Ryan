import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Generate Random Samples
def Ran_Sam(Beta,n,Std_dev):
    x = np.random.rand(n) * 100
    error = np.random.randn(n) * Std_dev
    y = x * Beta + error
    return {'x':x,'y':y}
    
# Lets say Beta (Slope) is 10, n is 20, with std_ dev of 100
Samples = Ran_Sam(10,20,100)

# Plot Random date
plt.figure(1)
plt.scatter(Samples['x'],Samples['y'])

# Find the averge of x and y
x_avg = np.average(Samples['x'])
y_avg = np.average(Samples['y'])

''' 
Using Equation 4 from the short document we will now find b_1
'''
# Initilize b_1 = 0
b_1t = 0 #top of equation 4
b_1b = 0 #bottom of equation 4
for i in range (0,len(Samples['x'])):
    b_1t += (Samples['x'][i]-x_avg)*(Samples['y'][i]-x_avg) 
    b_1b += pow((Samples['x'][i]-x_avg),2)
    
b_1 = b_1t/b_1b
    
''' 
Now we have b_1, we can find b_0, as shown in the document as Equation 5
'''
b_0 = y_avg - b_1 * x_avg

''' 
Now we have b_1 and b_0, lets plot the line
'''
Plot_samples = np.linspace(0,100,20) #use the sample number as n in Ran_Sam function

def Linear_Regression(Plot_samples,b_0,b_1):
    y_hat = b_0 + b_1 * Plot_samples
    return y_hat

y_hat = Linear_Regression(Plot_samples,b_0,b_1)

plt.plot(Plot_samples,y_hat)
plt.xlim([0,100])
plt.ylim([min(Samples['y'])-100,max(Samples['y'])+100])

''' 
We can also find the MSE
'''
y_hat_MSE = Linear_Regression(Samples['x'],b_0,b_1) #Uses the dependent variables of the samples

Sum_value = 0 #
for i in range(0,len(Samples['y'])): 
    Sum_value += pow((Samples['y'][i]-y_hat_MSE[i]),2)
    
MSE = (1/len(Samples['y']))*Sum_value
print('The Mean Squared Error is ' + str(MSE))

'''
NOTES:

There is an numpy sum function so you usually wouldnt have to do loops, but
since you're using Java, I don't know if there are any numpy copy libraries. 
So i just used loops for the sums

'''    





