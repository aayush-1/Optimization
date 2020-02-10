#Code by GVV Sharma, 
#Jan 13, 2020
#Released under GNU GPL
#Solving a quadratic program using cvx
from cvxpy import *
import numpy as np
import matplotlib.pyplot as plt
#Line parameters
n =  np.array([1,2]).reshape(2,-1)
P = np.array([2,1]).reshape(2,-1)
a=np.array([50,70]).reshape(2,-1)
x = Variable((2,1))
#Cost function
f =  a.T@x
obj = Minimize(f)
#Constraints

constraints = [P.T@x >=8,n.T@x>=10]

#solution
Problem(obj, constraints).solve()

print(f.value,x.value)

x1 = np.linspace(0,10,100)
x2 = (8*np.ones(100) - 2*x1)

x3 = np.linspace(0,10,100)
x4 = (10*np.ones(100) - x3)/2
plt.plot(x1,x2)
plt.plot(x3,x4)
plt.plot(0,8,'o')
plt.plot(2,4,'o')
plt.plot(10,0,'o')
plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.show()
