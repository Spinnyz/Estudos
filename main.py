def saudacao(saudacao,nome):
    def saudar():
        return f"{saudacao} {nome}"
    return saudar
        

s1 = saudacao("Bom dia","pedro")
print (s1())

