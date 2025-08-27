class ContaBancaria:
    def __init__ (self,titular, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar (self,valor):
        if valor > 0:
            self.saldo += valor
            print (f"O valor de {valor} foi depositado")
        else:
            print (f"O valor de {valor} não pode ser depositado")
        
    def sacar (self,valor):
        if valor > 0:
            self.saldo -= valor
            print (f"O valor de {valor} foi sacado")
        else:
            print (f"O valor de {valor} não pode ser sacado")
        
    def mostrar_saldo(self):
            print (f"O saldo atual é de {self.saldo}")

conta = ContaBancaria("Pedro")
while True:
    print("Escolha uma opção:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Mostrar saldo")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        conta.depositar(valor)  
    
    if opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        conta.sacar(valor)
    
    if opcao == "3":
        conta.mostrar_saldo()

        

