def bestSum(target, nums):
# def bestSum(target, nums):
    if memo is None: memo = {} # initialize memotrization
    if target in memo.keys(): return memo[target].copy() if memo[target] is not None else None  # memoization
    if target == 0: return []   # base case
    if target < 0:  return None # base case 2

    shortest_combo = []
    for n in nums:
        reminder = target - n
        # result = bestSum(reminder,nums)
        result = bestSum(reminder,nums,memo)

        if result is not None:
            result.append(n)
            if len(shortest_combo) ==0 or len(result) < len(shortest_combo):
                shortest_combo = result.copy()

    memo[target] = shortest_combo.copy() if len(shortest_combo) > 0 else None
    # print(target, memo)

    return memo[target].copy() if memo[target] is not None else None
    
if __name__ == '__main__':
    print([7],bestSum(7,[5,3,4,1,7])) # [3,4]
    print(None,bestSum(7,[2,4])) # None
    print(None,bestSum(300,[7,14])) # None
    print([50,50,50,50,50,50],bestSum(300,[10,25,2,14,5,6,68,50])) # True