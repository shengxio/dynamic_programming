def countConstruct(target, components,memo=None):
    if memo is None:    memo = {}
    if target == "":    return 1 # base case
    if target in memo:  return memo[target]
    
    memo[target] = sum([countConstruct(target.replace(c,"",1),components,memo) for c in components if c == target[:len(c)]])
    return memo[target]
        

if __name__ == '__main__':
    print(1,countConstruct("abcdef",["abc","cde","efg","cd","def"]))
    print(4,countConstruct("purple",["p","u","r","le","e","l","pur"]))
    print(0,countConstruct("skateboard",["bo","rd","a","sky"]))
    print(4,countConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
    print(0,countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eeee","eeeeeeeeeeee"]))