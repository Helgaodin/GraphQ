import numpy as np
import pylab
import matplotlib.pyplot as plt
address = 'C:/Users/Olga/Desktop/Щур Изинг/k10/'
step=[]
yMax =[]
q=["3", "31", "32", "37", "38", "39", "43", "44", "45", "46", "47", "48", "49", "5", "51", "52", "53", "54", "55"]
file = address+'Plot0.41.txt'
x =[]
y =[]
z=[]
k=0
for q0 in q:
    k=0
    file = address+'Plot0.' + q0 +'.txt'
    print(file)
    for line in open(file):
        if(k%3==0):
            z.append(np.array(line.split('\t')))#step
        if(k%3==1):
            x.append(np.array(line.split('\t')))#x
        if(k%3==2):
            y.append(np.array(line.split('\t')))#y
        k=k+1
    k
    step.append(z[len(z)-1].astype(np.float)[0])
    yAr = y[len(z)-1]
    yAr = yAr[:-1].astype(np.float)
    yMax.append(np.argmax(yAr))
print(step)
#print('0.'+q)
plt.plot([float('0.'+i) for i in q], [i/10 for i in yMax], 'bo')
plt.plot([float('0.'+i) for i in q], [i/10 for i in yMax])
plt.xlabel('q')
plt.ylabel('m')
plt.show()
