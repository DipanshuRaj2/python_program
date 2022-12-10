T = int(input())
M = 1000000007

from math import factorial, sqrt


def nck(n, k):
    res = 0
    
    for i in range(k+1):
        res += factorial(n)//(factorial(i)*factorial(n-i))
    return res


def divisors(n):
    d1 = [1]
    d2 = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            d1.append(i)
            if i*i != n:
                d2.append(n//i)    
    d1.extend(d2[::-1])
    return d1
        

for _ in range(T):
   
    N, K = [int(x) for x in input().split()]
    S = input()
    if N == 1:
        print(N+K)
        continue
    
    total = nck(N, K)
    div = divisors(N)
    dp = [[0]*(N+K+1) for i in range(len(div))]
    is_periodic = False
    
    for i, d in enumerate(div):
        dp[i][0] = 1
        for offset in range(d):
            zeros = 0
            
            for j in range(offset, N, d):
                if S[j] == "0":
                    zeros += 1
            ones = N//d - zeros  
            
            prev = list(dp[i])           
            dp[i][:] = [0]*(N+K+1)
            
            for k in range(K+1):
                if prev[k]:
                    dp[i][k + zeros] += prev[k]
                    dp[i][k + ones] += prev[k]
        
        if dp[i][0]:
            is_periodic = True
        
        for i2 in range(i):                
            d2 = div[i2]            
            if d % d2 == 0:
                for k in range(K+1):
                    dp[i][k] -= dp[i2][k]
                        
        for k in range(1, K+1):
            total -= dp[i][k]
    
    print((total-is_periodic) % M)