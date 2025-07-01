marks=int(input("enter a value:"))
if marks>=90:
    print("A+ Grade")
elif marks<=89 and marks>=75:
    print("A Grade")
elif marks<=74 and marks>=60:
    print("B Grade")
elif marks<=59 and marks>=35:
    print("C Grade")
else:
    print("Student is Failed")