def canConstruct(target, components):
    if target == "":    return True # base case
    
    table_form = {i:False for i in range(len(target)+1)}
    table_form[0] = True
    for i in table_form:
        for c in components:
            if i >= len(c) and target[i-len(c):i]==c:
                table_form[i] = table_form[i] or table_form[i-len(c)]
    return table_form[len(target)]

    # m = target size
    # n = components size
    # time complexity: O(m^2*n)
    # space complexity: O(m)
        

if __name__ == '__main__':
    print(True,canConstruct("abcdef",["abc","cde","efg","cd","ef"]))
    print(False,canConstruct("skateboard",["bo","rd","a","sky"]))
    print(True,canConstruct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
    print(False,canConstruct("eeeeeeeeeeeeef",["e","ee","eeee","eeeeeeeeeeee"]))