import numpy as np
print "-------"
a = np.zeros((3,12))
new_arry = np.reshape(a,(3,3,2,2))
#print new_arry
a = np.zeros(12)
b = np.ones(12)

c = np.random.random_sample(12)
'''
print b
print c
'''
d = np.vstack((a,b,c))


print d
e = np.reshape(d,(3,3,2,2))
print e

f = np.random.random_sample(4)
g = np.random.random_sample(4)
print f
print g
print "--"
f1 =  np.reshape(f,(2,2))
g1 = np.reshape(g,(2,2))
h1 = np.zeros((2,2))
print f1
print g1
print "---"
z = np.stack((f1,g1,h1))
print z
print '---'
z1= np.array([f1,g1,h1])
print z1
print z-z1
print z1.shape

vec1=np.zeros(300)
vec2=np.ones(300)
vec11 = np.reshape(vec1,(3,10,10))
vec21 = np.reshape(vec2,(3,10,10))
vec = np.stack((vec11,vec21))
print vec.shape

'''

test=range(300)
testarry = np.array(test)
print testarry
t1 = np.reshape(testarry,(3,10,10))
print t1'''