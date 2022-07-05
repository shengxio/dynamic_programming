def bestSum(target, nums):
    if target == 0: return []   # base case
    if target < 0:  return None # base case 2

    array_nums = {n:None for n in range(target + 1)}
    array_nums[0] = []

    for i in range(target + 1):
        for j in nums:
            if i -j >=0 and array_nums[i-j] is not None:
                result = array_nums[i-j] + [j]

                if array_nums[i] is None:
                    array_nums[i] = result

                if len(array_nums[i]) > len(result):
                    array_nums[i] = result
    return array_nums[target]
                
if __name__ == '__main__':
    print([7],bestSum(7,[5,3,4,1,7])) # [3,4]
    print(None,bestSum(7,[2,4])) # None
    print(None,bestSum(300,[7,14])) # None
    print([50,50,50,50,50,50],bestSum(300,[10,25,2,15,5,6,68,50])) # True