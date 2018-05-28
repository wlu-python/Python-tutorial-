
import matplotlib.pyplot as plt
import random


y=[]
a=[]
x = range(20)
#y = [1, 3, 5]
for z in x:
	alpha=random.randint(-3,3)
	a.append(alpha)
	numb=2*z+5+alpha
	y.append(numb)
for z in range(0,len(x)):
	print("%i,%i,%i" %(x[z],y[z],a[z]))

plt.plot(x, y)
plt.show()
