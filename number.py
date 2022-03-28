def max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1, 'maximum number.'
    elif n2 >n1 and n2 > n3:
        return n2,'maximum number.'
    elif n3 > n1 and n3 > n2:
        return n3, 'maximum number.'
    else:
        pass
def min(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1, 'minimum number'
    elif n2 < n1 and n2 < n3:
        return n2, 'minimum number.'
    elif n3 < n1 and n3 < n2:
        return n3, 'minimum number.'
    else:
        pass

num1 = int(input("1st Number: "))
num2 = int(input("2nd Number: "))
num3 = int(input("3rd Number: "))

print(max(num1, num2, num3))
print(min(num1, num2, num3))
