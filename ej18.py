import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt("valores.txt")
x=datos[:,0]
y=datos[:,1]


t=np.linspace(0,3,100)
analitic=np.exp(-t)

plt.scatter(x,y)
plt.plot(t,analitic)
plt.savefig("primerord.pdf")
