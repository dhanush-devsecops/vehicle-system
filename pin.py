pin="3214"
attempts=3
while attempts>0:
    user_pin=input("enter a value:")
    if len(user_pin)!=4:
        print("Please check the length of the pin")
    elif pin==user_pin:
        print("Unlocked")
        break
    else:
        attempts-=1
        print("Access Denied")
        if attempts>0:
            print(f"{attempts} attempt(s) remaining")
        else:
            print("Your Card Is Blocked!!")