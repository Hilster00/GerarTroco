memo=dict()
def troco(valor=0,moedas=[1,5,10,25,50]):
    global memo
    if valor < 0:
        return None
    if valor == 0:
        return 0
    if memo.get(valor) != None:
        return memo[valor]
    memo[valor]=1+min([troco(valor-i) if valor >= i else float('infinity') for i in moedas])
    return memo[valor]
