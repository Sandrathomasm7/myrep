n= input("Enter the number:")
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
