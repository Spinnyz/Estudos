def executa (funcao, *args):
    return funcao(*args)

def soma (x,y):
        return x+y
    
def criar_mult(multiplicador):
        def multiplica(valor):
            return valor*multiplicador
    
        return multiplica


print (
    executa (
        lambda multiplicador,valor : valor*multiplicador, 3,2
    ),
    executa (criar_mult(3),2)
)