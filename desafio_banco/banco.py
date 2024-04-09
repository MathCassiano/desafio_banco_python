menu = """
        [d] - Depositar
        [s] - Sacar
        [e] - Extrato
        [q] - Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: "))
        
        if(valor > 0):
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor não pode ser um vao negativo, tente novamente.")
    
    if opcao == "s":
        valor = float(input("Informe um valor valor a ser sacado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excendeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        
        elif excedeu_limite:
            print("Limite insuficiente!")
        
        elif excendeu_saques:
            print("Excedido o número de saques diário")
        
        elif(valor > 0):
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou, o valor informado é invalido")
    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        break
    
    else: 
        print("Opção inválida!")


