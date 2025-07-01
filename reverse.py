import time
import sys
n=input("enter a value:")
start=time.time()
rev=n[::-1]
print("Reversed Value:",rev)
end=time.time()
print("Execution Time:",end-start,"seconds")
print("Size of num:",sys.getsizeof(n),"bytes")
print("Size of num:",sys.getsizeof(rev),"bytes")