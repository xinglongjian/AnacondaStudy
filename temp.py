# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pylab as plt
X=[[65],[67],[78],[80],[94],[115]]
Y=[[320],[360],[400],[415],[500],[570]]
plt.figure()
plt.title('Price of House Against Area')
plt.xlabel('Area(square meter)')
plt.ylabel('Price(ten thousand)')
plt.plot(X,Y,'r.')
#plt.axis([0,150,0,600])
plt.grid(True)
#plt.show()

from sklearn.linear_model import LinearRegression
#create and fit the model
model=LinearRegression()
model.fit(X,Y)
print('A 85 m^2 house should sale : %.2f w ' % model.predict([85])[0])
X_Test=[[45],[85],[125]]
plt.plot(X_Test, model.predict(X_Test), 'b-',linewidth=1)
plt.show()

