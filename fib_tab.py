def fib(n:int):
    tabula = {i:0 for i in range(0,n+1)}
    
    for i in range(0,n+1):
        if i == 0:
            tabula[i] = 0
        elif i == 1:
            tabula[i] = 1
        
        if i+1 <= n:
            tabula[i+1] += tabula[i]
        if i+2 <= n:
            tabula[i+2] += tabula[i] 

    return tabula[n]

if __name__ == '__main__':
    print(fib(6))
    print(fib(100))