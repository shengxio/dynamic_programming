def canSum(n:int,numbers:list,memo:dict=None):
    if memo is None: memo = {} # initialize memotrization
    if n < 0:   return False # base case 2
    if n == 0:  return True # base case
    if n in memo.keys(): return memo[n] # memoization

    memo[n] = any([canSum(n-m,numbers,memo) for m in numbers])
    print(n,memo[n])

    return memo[n]

if __name__ == '__main__':
    print("True",canSum(7,[5,3,4,7])) # True
    print("False",canSum(7,[2,4])) # False
    # print("False",canSum(300,[7,14])) # False
    # print("True",canSum(300,[7,14,25,2,45])) # True