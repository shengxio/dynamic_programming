def howSum(target, nums, memo=None):
# def howSum(target, nums): #,memo=None):
    if memo is None: memo = {} # initialize memotrization
    if target in memo.keys(): return memo[target] # memoization
    if target == 0: return []   # base case
    if target < 0:  return None # base case 2

    for n in nums:
        reminder = target - n
        result = howSum(reminder,nums,memo)

        if result is not None:
            memo[target] = result
            memo[target].append(n)
            return memo[target]

    memo[target] = None
    return memo[target]
    # m = target size
    # n = nums size
    # time complexity: O(m^2*n)
    # space complexity: O(m^2)    
    
if __name__ == '__main__':
    print([3,4],howSum(7,[5,3,4,7])) # [3,4]
    print(None,howSum(7,[2,4])) # None
    print(None,howSum(300,[7,14])) # None
    print(True,howSum(300,[7,14,25,2,45])) # True