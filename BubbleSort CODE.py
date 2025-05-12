A = [21, 45, 67, 129, 23, 76, 82, 88]
n = len(A) 

for j in range(0,n):
  
  for i in range(0,n-1):
    if A[i] > A[i+1] :
      temp = A[i]
      A[i] = A[i+1]
      A[i+1] = temp

print(A)
