n = int (input ("No.of elements in array:\n"))
print ("Enter the numbers you want your array to have:")

arr = []
for _ in range(n) :
	arr.append(int (input()))

for i in range (1, len(arr)):
	k = arr[i]
	j = i-1
	while ((j>=0) and (arr[j]>k)):
		arr[j+1] = arr[j]
		j = j-1
	arr[j+1] = k
print ("Sorted array is:")
for x in arr:
	print(x)
