import os
def fun(arr):
	ans = 0
	for i in range(1, len(arr)):
		ans = max(ans, arr[i] - arr[i - 1])
	return ans
s = input()
arr = []
for x in os.listdir(s):
	file_path = s + "/" + x
	arr.append(os.path.getsize(file_path))
	
arr = sorted(arr)

print(arr)
print("K4",arr[0])
print("K5",arr[-1])
print("K6",arr[-1] - arr[0])
print("K7", fun(arr))