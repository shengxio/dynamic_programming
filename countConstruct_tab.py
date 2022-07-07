def countConstruct(target, components):
    if target == "":    return 1 # base case
    
    construct_table = {i:0 for i in range(len(target)+1)}
    construct_table[0] = 1

    for i in range(len(target)+1):
        for c in components:
            if i >= len(c) and target[i-len(c):i] == c:
                construct_table[i] += construct_table[i-len(c)]

    return construct_table[len(target)]

    # m = target size
    # n = components size
    # time complexity: O(m^2*n)
    # space complexity: O(m)
        

if __name__ == '__main__':
    print(1,countConstruct("abcdef",["abc","cde","efg","cd","def"]))
    print(4,countConstruct("purple",["p","u","r","le","e","l","pur"]))
    print(0,countConstruct("skateboard",["bo","rd","a","sky"]))
    print(4,countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
    print(0,countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eeee","eeeeeeeeeeee"]))