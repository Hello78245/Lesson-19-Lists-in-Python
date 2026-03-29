L=[4,21,30,10,60]
print("Original list of numbers:",L)
count=0
for i in L:
    count+=i
avg=count/len(L)
print("Sum is:",count)
print("Average is:",avg)
L.sort()
print("Maximum is:",L[0])
print("Minimum is:",L[-1])