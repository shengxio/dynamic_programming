def gridTravel(m:int,n:int,grid:dict={}):
    if m <= 0 or n <= 0: # out of range
        return 0

    if m == 1 and n == 1: # base case
        return 1

    if (m,n) in grid.keys(): # memoization
        return grid[(m,n)]

    grid[(m,n)] = gridTravel(m-1,n,grid) + gridTravel(m,n-1,grid) # recursive call

    return grid[(m,n)]
    # time complexity: O(m*n)
    # space complexity: O(m+n)

if __name__ == '__main__':
    print(gridTravel(50,50))