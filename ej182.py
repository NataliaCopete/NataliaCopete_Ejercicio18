import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt("valores2.txt")
x=datos[:,0]
y=datos[:,1]
z=datos[:,2]


t=np.linspace(0,10,100)
analitic=np.cos(t)

plt.scatter(x,y)
plt.plot(t,analitic)
plt.savefig("segundord.pdf")
plt.clf()
plt.scatter(z,y)
plt.savefig("Zvsy")

