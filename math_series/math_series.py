def  Fibonacci_Series(n):
    if n==1 or n==2:
        return 1
    if n==0:
        return 0
    else:
        return Fibonacci_Series(n-1)+Fibonacci_Series(n-2)


def  Lucas_Numbers(n):
    if n==0 :
        return 2
    if n==1:
        return 1   
    else:
        return Lucas_Numbers(n-1)+Lucas_Numbers(n-2)             
def sum_series(n,x=0,y=1):
    if n==0:
        return x
    if n==1:
        return y
    else :
        return  sum_series(n-1,x,y)+sum_series(n-2,x,y) 
"""
   sum(3)+sum(2)
   sum(2)+sum(1)+sum(2)
sum(1)+sum(0)+2+sum(1)+sum(0)
(4,3,4)
sum_series(3)+sum_series(2)
   """