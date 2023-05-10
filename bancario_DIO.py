from time import sleep
delay = 1
delaay = 1.5

## inicio do programa
print("=========== BEM VINDO AO NOSSO SISTEMA BANCARIO =========== ")

## Menú inicial
menu = """
================= SELECIONE UMA DAS OPÇÕES ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair do sistema
===========================================================s

=> """

## Variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu)    
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            print("----------------------------------------------------")
            sleep(delay)
            print("Seu depósito foi efetuados com sucesso! ")
            saldo += valor
            sleep(delay)
            print("seu saldo em conta é de R$", saldo)
            print("\n\n")
            extrato += f"Deposito: R$ {valor:.2f}\n"
            sleep(delaay)
        
            
        else:
            print("operação falhou! O valor informado é inválido. ")
            sleep(delaay)
            
            
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque. "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente. ")
            sleep(delaay)
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite. ")
            sleep(delaay)
            
        elif excedeu_saques:
            print("Operação falhou! Numero maximo de saques excedido. ")
            sleep(delaay)
            
        elif valor > 0:
            print("----------------------------------------------------")
            sleep(delay)
            print("Seu saque foi efetuados com sucesso! ")
            sleep(delaay)
            
            saldo -= valor
            sleep(delay)
            print("seu saldo em conta é de R$", saldo)
            print("\n\n")

            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            sleep(delaay)
            
        else:
            print("Operação falhou! o valor informado é inválido. ")
            sleep(delaay)
        
        
    elif opcao == "e":
        print("\n==================== EXTRATO =======================")
        sleep(delay)
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        sleep(delay)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================================")
        sleep(delaay)
        
        
    elif opcao == "q":
        print("Agradecemos pela preferencia, até logo!")
        sleep(delay)
        break
    
    else:
        sleep(delay)
        print("Operação inválida, por favor selecione novamente a opção desejada. ")