n=int(input("Enter the number of elements:"))
print('Enter the elements')
arr = []
flag = 0
for _ in range(n):
	x=int(input())
	arr.append(x)
num=int(input("Enter a num:"))
for i in arr:
	if(i == num):
		flag = 1
		break
if(flag == 1):
	print("element is present")
else:
	print("element is not present")
	
