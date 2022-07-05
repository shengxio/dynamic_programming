def canConstruct(target, components):
    if target == "":    return True # base case
    
    result = any([canConstruct(target.replace(c,"",1),components) for c in components if c == target[:len(c)]])
    return result
        

if __name__ == '__main__':
    print(True,canConstruct("abcdef",["abc","cde","efg","cd","ef"]))
    print(False,canConstruct("skateboard",["bo","rd","a","sky"]))
    print(True,canConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
    print(False,canConstruct("eeeeeeeeeeeeef",["e","ee","eeee","eeeeeeeeeeee"]))