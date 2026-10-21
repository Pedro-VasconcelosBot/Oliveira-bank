# banco digital versão 1

saldo = 1300
print("===OLIVEIRA BANK===")

deposito = float(input("Qual valor deseja depositar? "))
saque = float(input('E qual o valor do Saque agora? '))

saldo = saldo + deposito
novoSaldo = saldo

if saque <= 0 or saque > saldo:
    print ('Saque Indisponível!')
else:
    novoSaldo = saldo - saque
    print('Saque realizado com sucesso!')

print("Seu saldo Atualizado é de: R$ ", novoSaldo)

