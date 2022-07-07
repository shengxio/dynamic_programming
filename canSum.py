def canSum(target:int,numbers:list,memo:dict=None):
    if memo is None: memo = {} # initialize memotrization
    if target < 0:   return False # base case 2
    if target == 0:  return True # base case
    if target in memo.keys(): return memo[target] # memoization

    memo[target] = any([canSum(target-m,numbers,memo) for m in numbers])
    print(target,memo[target])

    return memo[target]
    # m = target size
    # n = numbers length
    # time complexity: O(m*n)
    # space complexity: O(m)

if __name__ == '__main__':
    print("True",canSum(7,[5,3,4,7])) # True
    print("False",canSum(7,[2,4])) # False
    # print("False",canSum(300,[7,14])) # False
    # print("True",canSum(300,[7,14,25,2,45])) # True