def prime(num):
    if num>1:
        for i in range(2,num):
            if num %i ==0:
                return "Its not a prime number"
            else:
                return "yes its a prime number"
        else:
            return "its is not a prime number"

num= int(input("Please enter your number: "))
print(prime(num))