def fib(n:int,memo:dict={}):
    if n <=0: # out of range
        return 0
    
    if n <= 2: # base case
        return 1

    if n in memo.keys(): # memoization
        return memo[n]
    
    memo[n]=fib(n-1,memo) + fib(n-2,memo) # recursive call

    return memo[n]
    # time complexity: O(n)
    # space complexity: O(n)

if __name__ == '__main__':
    print(fib(6))
    print(fib(100))