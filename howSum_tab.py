def howSum(target, nums):
    if target < 0:  return None # base case 2

    table_dict = {i:None for i in range(target+1)}
    table_dict[0] = []

    for i in range(target+1):
        for j in nums:
            if i-j >= 0 and table_dict[i-j] is not None:
                    table_dict[i] = table_dict[i-j] + [j]
                    if i == target:
                        return table_dict[i]
    
if __name__ == '__main__':
    print([3,4],howSum(7,[5,3,4,7])) # [3,4]
    print(None,howSum(7,[2,4])) # None
    print(None,howSum(300,[7,14])) # None
    print([],howSum(300,[7,14,25,2,45])) # []