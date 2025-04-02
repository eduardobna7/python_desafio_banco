LIMITE_SAQUES=2 #são 3, mas comecei com o 2 por conta do tipo de contagem do python
LIMITE=500
extrato=""
saldo=0
numero_saques=0

menu=""" digite [1] para sacar
         digite [2] para pedir extrato
         digite [3] para depositar
         digite [0] para sair\n"""

while True:
    opcao=int(input(menu))
    if opcao==1:
       saque=float(input("valor do saque: "))
       excedeu_saldo = saque > saldo
       excedeu_limite = saque > LIMITE
       excedeu_numero_saques = numero_saques > LIMITE_SAQUES
       
       if excedeu_saldo:
           print("Saldo insuficiente para realizar o saque.")
       elif excedeu_limite:
           print("Limite insuficiente para realizar o saque.")
       elif excedeu_numero_saques:
           print("Você excedeu o número diário de saques.")
       elif saque > 0:
           print("saque realizado com sucesso") 
           saldo-=saque
           numero_saques += 1
           extrato+=f"Saque no valor de {saque:.2f}\n"
       else:
           print("operação inválida.")
           

    elif opcao==2:
        print("extrato: ")

    elif opcao==3:
       deposito=float(input("depósito: "))
       if deposito>0:
           saldo+=deposito
           extrato+=f"Depósito no valor de {deposito:.2f}\n"
       else:
           print("não foi possível realizar o depósito.")

    elif opcao==0:
        break
    else:
        print("Opção inválida, tente novamente.\n")