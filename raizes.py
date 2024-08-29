from math import sqrt

def raiz(a,b,d):
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-d**0.5)/(2*a)
    return x1,x2