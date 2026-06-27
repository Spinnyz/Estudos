quiz= [
    {
    "pergunta": "1+1",
    "resposta": [1,2,3,4],
    "correta": 1,
    },
    
    {
    "pergunta": "10x20",
    "resposta": [10,200,300,400],
    "correta": 200,
    },
    
    {
    "pergunta": "10x40",
    "resposta": [10,200,300,400],
    "correta": 400,
    }

]
    
    
escolher = 0

for i in quiz:
    print (quiz[escolher]["pergunta"])
    print (quiz[escolher]["resposta"])

    user = input("RESPOSTA: ")

    if user.isdigit():
        if user != quiz[escolher]["correta"]:
            print ("errado")
    
        else:
            print ("correto")
    else:
        print ("Valor invalido, nao digite letras")

    escolher +=1
