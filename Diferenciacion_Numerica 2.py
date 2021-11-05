import numpy as np
import pylab as pl
from scipy.interpolate import lagrange 

x= np.array([1,-3,5,7 ])
y= np.array([-2,1,2,-3 ])
PolLangrage= lagrange(x,y)
xPol=np.linspace(np.min(x),np.max(x),20,endpoint=True)
print(xPol)
#print(PolLangrage(1))

pl.plot(x,y,"o")
pl.show()
