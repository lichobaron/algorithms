
from random import randint, uniform
import numpy as np
import matplotlib.pyplot as plt

def GenerarPuntos (p1,p2,n):
    puntos = []
    for i in range (n+1):
        x = uniform(p1[0],p2[0])
        y = uniform(p1[1],p2[1])
        t = (x,y)
        puntos.append(t)
        plt.scatter(x,y)
    S = convex_hull(puntos)
    return S

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

p1 = [0,0]
p2 = [9,9]
n = 100
P = GenerarPuntos(p1,p2,n)
X = []
Y = []
for a,b in P:
    X.append(a)
    Y.append(b)
t = P[0]
X.append(t[0])
Y.append(t[1])
plt.plot(X,Y)    
plt.show()