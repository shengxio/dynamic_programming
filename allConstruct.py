def allConstruct(target, components,memo=None):
    if memo is None:    memo = {}
    if target == "":    return [[]] # base case
    if target in memo:  return memo[target]
    
    memo[target] = []
    for c in components:
        if target.startswith(c):
            ls_temp = [[c] + s for s in allConstruct(target[len(c):], components, memo)]
            memo[target] += ls_temp

    return memo[target]
    # m = target size
    # n = components size
    # time complexity: O(n^m)
    # space complexity: O(m^2)
        

if __name__ == '__main__':
    print([["abc","def"]],allConstruct("abcdef",["abc","cde","efg","cd","def"]))
    print([
        ["pur","p","le"],
        ["p","u","r","p","le"],
        ["pur","p","l","e"],
        ["p","u","r","p","l","e"]],
        allConstruct("purple",["p","u","r","le","e","l","pur"]))
    print([],allConstruct("skateboard",["bo","rd","a","sky"]))
    print([
        ["enter","a","p","o","t","ent","p","o","t"],
        ["enter","a","p","ot","ent","p","o","t"],
        ["enter","a","p","o","t","ent","p","ot"],
        ["enter","a","p","ot","ent","p","ot"]],
        allConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
    print([],allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eeee","eeeeeeeeeeee"]))