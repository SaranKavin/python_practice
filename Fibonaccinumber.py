def fib(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)  # Compute & store
    return memo[n]

def fun(n, m):
    count, idx = 0, 2  # Counter & index starting from the third Fibonacci number
    
    while True:
        value = fib(idx)  # Compute Fibonacci number
        
        if value % m == 0: 
            count += 1
            if count == n:  
                return value  
        
        idx += 1  # Move to the next index

n, m = 4, 3  # 4th Fibonacci multiple of 3
print(fun(n, m))
