
import matplotlib.pyplot as plt
import random


y=[]
y2=[]
a=[]
delta=0
x = range(20)
#y = [1, 3, 5]
for z in x:
	alpha=random.randint(-3,3)
	a.append(alpha)
	delta=delta+alpha	
	numb=2*z+5+alpha
	y.append(numb)
	numb=2*z+5+delta
	y2.append(numb)


for z in range(0,len(x)):
	print("%i,%i,%i,%i" %(x[z],y[z],y2[z],a[z]))

plt.plot(x, y)
plt.plot(x, y2)

plt.show()
