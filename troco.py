valores=[1,2,3,4,5,6,7,10,15,20,25,30,49,50,74,99]
memo=dict()
def troco(valor):
    if valor < 0:
        return float('infinity')
    if valor == 0:
        return 0
    if memo.get(valor) != None:
        return memo[valor]
    memo[valor]=1+min([troco(valor-i) for i in valores])
    return memo[valor]
