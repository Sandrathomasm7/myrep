def array():
	print('\t\tpgm to check whether a given no. is present in the array or not')
	print('\t\t--------------------------------------------------------------\n')
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

def prime():
	print('\n\t\tpgm to check whether a given number is prime')
	print('\t\t-------------------------------------------\n')
	n=input("Enter the number:")
	if n > 1:
		flag = 0
		for i in range(2, n//2+1):
			if (n % i) == 0:
				flag = 1
				break
		if(flag == 1):
			print(n, "is not a prime number")
		else:
			print(n, "is a prime number")

	else:
		print(n, "is not a prime number")
			
def string():
	print('\n\t\tpgm for replacing the string in a text file')
	print('\t\t--------------------------------------------')
	file1=open("sample.txt","r")
	if file1.mode == 'r':
		file_contents = file1.read()
	print (file_contents)
	file1.close()
	str1 = raw_input("Enter the first string:")
	str2 = raw_input("Enter the first string:")
	print("string1:",str1)
	print("string2:",str2)
	file1=open("sample.txt","r")
	file_contents = file1.read()
	newdata = file_contents.replace(str1,str2)
	file1=open("sample.txt","w+")
	file1.write(newdata)
	file1.close()
	file1=open("sample.txt","r")
	file_contents = file1.read()
	print (file_contents)

array()
prime()
string()
