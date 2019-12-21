import numpy as np
import matplotlib.pylab as plt
plt.show()
# values from -4pi to 4pi
x=np.arange(-4*np.pi,4*np.pi,0.05)
y_sin=np.sin(x)
y_cos=np.cos(x)

#Drawing sin and cos functions
plt.plot(x,y_sin,color='red',linewidth=1.5, label="Sin(x)")
plt.plot(x,y_cos,color='blue', label="Cos(x)")
plt.title("Sin vs Cos graph")
plt.xlabel('Angles in radian')
plt.ylabel('sin(x) and cos(x)')
plt.legend(['sin(x)','cos(x)'])
plt.show()
