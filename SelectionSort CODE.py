A = [11, 52, 76, 92, 53, 26,12, 48]
n = len(A) 

for i in range(0,n):
  min = i
  for j in range(i+1,n):
    if A[j] < A[min] :
      min = j
  if min != i:
    temp = A[i]
    A[i] = A[min]
    A[min] = temp

print(A)
