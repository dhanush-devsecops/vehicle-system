import time
import sys
n=input("enter a value:")
start=time.time()
if n==n[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
end=time.time()
print("Execution Time:",end-start,"seconds")
print("Size of",sys.getsizeof(n),"bytes")