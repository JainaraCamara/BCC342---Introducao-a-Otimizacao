import math


def golden_search(f,a,b,tol):

    gr = (1 + math.sqrt(5))/2

    c = b - (b-a)/gr
    d = a + (b-a)/gr


    while abs(b-a) > tol
       if f(c) > f(d)
           a = c
       else:
           b = d

        c = b - (b-a)/gr
        d = a + (b-a)/gr

    return (b+a)/2

