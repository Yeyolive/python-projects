A = [21, 25, 67, 89, 3, 46, 2, 8]
n = len(A) 

for i in range(1, len(A)):
  
        key = A[i]
        j = i-1
        while j >=0 and key < A[j] :
                A[j+1] = A[j]
                j -= 1
        A[j+1] = key

print(A)        
  
