def canSum(n:int,numbers:list):
    if n < 0:   return False # base case 2

    table_dict = {i:False for i in range(n+1)}
    table_dict[0] = True
    for i in range(n+1):
        for j in numbers:
            if i-j >= 0:
                table_dict[i] = table_dict[i] or table_dict[i-j]
    
    return table_dict[n]

if __name__ == '__main__':
    print("True",canSum(7,[5,3,4,7])) # True
    print("False",canSum(7,[2,4])) # False
    print("False",canSum(300,[7,14])) # False
    print("True",canSum(300,[7,14,25,2,45])) # True