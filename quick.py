
def partition(arr, l, h):
	i = l-1
	pivot = arr[h]
	for j in range (l, h):
		if arr[j] < pivot :
			i = i+1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
	temp1 = arr[i+1]	
	arr[i+1] = arr[h]
	arr[h] = temp1
	return (i+1)

def Quick (arr, l, h):
	if l<h :
		index = partition (arr, l ,h)
		Quick(arr, l, index-1)
		Quick(arr, index+1, h)


n = int (input ("No.of elements in array:\n"))
print ("Enter the numbers you want your array to have:")

arr = []
for _ in range(n) :
	arr.append(int (input()))

Quick (arr, 0, n-1)
print ("sorted array is:")
for x in arr :
	print (x)
