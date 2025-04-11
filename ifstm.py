a=int(input("enter the A value:"))
b=int(input("enter the B value:"))
c=int(input("enter the C value:"))
if(a>b):
    if(a>c):
       	print("A is Biggest value")
    else:
        print("C is Biggest value")
elif(b>a):
    if(b>c):
        print("B is Biggest value")
    else:
        print("C is Biggest value")
