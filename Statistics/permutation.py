# p(n,r)= n!/(n-r)!

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        result=1
        for i in range(2, n+1):
            result = result*i
        return result
    
def permutation(n,r):
    return fact(n)//fact(n-r)

n=5
r=3
print(f"Permutation for {r} items from {n} items: {permutation(n,r):.0f}")