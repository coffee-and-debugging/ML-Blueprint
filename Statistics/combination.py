# c(n,r)= n!/r!(n-r)!

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        result=1
        for i in range(2, n+1):
            result= result*i
        return result
    
def combination(n,r):
    return fact(n)/(fact(r)*fact(n-r))

n=5
r=3
print(f"Combination for {r} items from {n} total items: {combination(n,r):.0f}")