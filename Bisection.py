def Bisectionmethod(x):
    return  (x**3)-(2*x**2)-4
a=2
b=3
print("Bisectionmethod")
for i in range(1,20):
    x0=(a+b)/2
    print(x0)
    fx0=Bisectionmethod(x0)
    fa=Bisectionmethod(a)
    fb=Bisectionmethod(b)
    if fa*fx0<0:
        b=x0
    else:
        a=x0
