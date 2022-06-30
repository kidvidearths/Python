def bubbleSort(ar):
   n = len(ar)
   for i in range(n):
    for j in range(0, n-i-1):
      if ar[j] > ar[j+1] :
         ar[j], ar[j+1] = ar[j+1], ar[j]
ar = [52,5,34,22,54,51]
bubbleSort(ar)
print ("Sorted array is:", ar)