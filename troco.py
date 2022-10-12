valores=[1,2,3,4,5,6,7,10,15,20,25,30,49,50,74,99]
memo=dict()
def troco(valor=0):
    if valor < 0:
        return None
    if valor == 0:
        return 0
    if memo.get(valor) != None:
        return memo[valor]
    quantidade=list()
    for i in valores:
        if valor < i:
            break
        quantidade.append(troco(valor-i))
    memo[valor]=1+min(quantidade)
    return memo[valor]
