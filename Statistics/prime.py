def prime_ho_ki_naai(x):
    if x<2:
        return "Not prime"
    for i in range(2, x):
        if x%i==0:
            return "Not prime"
    return "Prime Number"

x=10
print(prime_ho_ki_naai(x))


def prime_nikalam(x):
    if x<2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True      
        
numbers=[1,2,3,4,5,6,7,8,9,10,11]
print([x for x in numbers if prime_nikalam(x)])