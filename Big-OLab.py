

def binarySearch(BigOlab_list,key):
    low = 0
    high = len(BigOlab_list) - 1

    while high >= low:
        mid = (low + high)//2
    if key > BigOlab_list[mid]:
        low = mid + 1
    elif key < BigOlab_lista[mid]:
        high = mid - 1
    elif key == BigOlab_list[mid]:
        return mid
        return -low-1


import random
import timeit



f = open("listlog.csv","w")

y = 1000000

f.write("n,T\n")

for i in range(10):

    BigOlab_list = random.sample(range(1,5000000),y)
    key = random.randrange(1,5000000,1)
  

BigOlab_list.sort()
  

start = timeit.default_timer()
binarySearch(BigOlab_list,key)
time_taken = timeit.default_timer() - start
f.write(str(y)+","+str(time_taken)+"\n")
  

y = y + 1000000


f.close()
