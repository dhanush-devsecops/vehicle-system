a=float(input("enter A value:"))
b=float(input("enter B value:"))
op=input("Choose Operation(+,-,*,/):")
if op=="+":
    print("result:",a+b)
elif op=="-":
    print("result:",a-b)
elif op=="*":
    print("result:",a*b)
elif op=="/":
    print("result:",a/b)
else:
    print("Invalid Operator")