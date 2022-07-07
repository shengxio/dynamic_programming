def allConstruct(target, components):
    import time
    start = time.time()
    if target == "":    return [[]] # base case

    construct_table = {i:None for i in range(len(target)+1)}
    construct_table[0] = [[]]

    for i in range(len(target)+1):
        for c in components:
            if i >=len(c) and target[i-len(c):i] == c and construct_table[i-len(c)] is not None:
                if construct_table[i] is None:
                    construct_table[i] = [[c] + s for s in construct_table[i-len(c)]]
                else:
                    construct_table[i] += [[c] + s for s in construct_table[i-len(c)]]

    # print(time.time()-start)
    return construct_table[len(target)]
    
    # m = target size
    # n = components size
    # time complexity: O(n^m)
    # space complexity: O(n^m)
        

if __name__ == '__main__':
    print(1,len(allConstruct("abcdef",["abc","cde","efg","cd","def"])))
    print(4,len(allConstruct("purple",["p","u","r","le","e","l","pur"])))
    print([],allConstruct("skateboard",["bo","rd","a","sky"]))
    print(4,len(allConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"])))
    print([],allConstruct("eeeeeeeeeeeeeeeef",["e","ee","eeee","eeeeeeeeeeee"]))