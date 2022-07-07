def gridTravel(m:int,n:int):
    if m <= 0 or n <= 0: # out of range
        return 0

    grid = {(i,j):0 for i in range(m+1) for j in range(n+1)}    
    grid[(1,1)]=1 # initial case

    for i in range(m+1):
        for j in range(n+1):
            if i+1 <=m:
                grid[(i+1,j)] += grid[(i,j)]
            if j+1 <=n:
                grid[(i,j+1)] += grid[(i,j)]

    return grid[(m,n)]
    # m = grid x size
    # n = grid y size
    # time complexity: O(m*n)
    # space complexity: O(m*n)

if __name__ == '__main__':
    print(1,gridTravel(1, 1))
    print(2,gridTravel(2,2))
    print(3,gridTravel(2,3))
    print(3,gridTravel(3,2))
    print(6,gridTravel(3,3))
    print(20,gridTravel(4,4))
    print("?",gridTravel(50,50))