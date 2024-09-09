transacoes = []  # Lista para armazenar o histórico de transações
extrado = 500
numero_de_saque = 0
limite_transacoes = 10
limite_valor = 500.00
# Função de saque
def sacar(saldo = extrado, valor_saque = 00.00, numero_de_saques = numero_de_saque, limite_saques = limite_transacoes, limite_valor = limite_valor):
    valor_saque = float(input('Digite o valor do saque: R$'))
    if valor_saque > saldo:
        return saldo, "Saldo insuficiente"
    elif valor_saque > limite_valor:
        return saldo, "Valor de saque excede o limite permitido"
    elif numero_de_saques >= limite_saques:
        return saldo, "Limite de saques diários atingido"
    else:
        saldo -= valor_saque
        numero_de_saques += 1
        transacoes.append(f"Saque de R${valor_saque:.2f}")
        limite_saques -= 1
        return f"Saque de {valor_saque:.2f} realizado com sucesso \nLimite de transações {limite_saques}"

# Função de depósito
def depositar(saldo = extrado, valor_deposito = 00.00, limite_deposito = limite_transacoes):
    valor_deposito = float(input('Digite o valor do depósito: R$'))
    if valor_deposito > 0 and valor_deposito <= 500:
        saldo += valor_deposito
        transacoes.append(f"Depósito de R${valor_deposito:.2f}")
        limite_deposito -= 1
        return f"Depósito de {valor_deposito} realizado com sucesso \nLimite de transações {limite_deposito}"
    else:
        return "Valor de depósito inválido"

# Função de visualização de histórico
def exibir_extrado():
    if not transacoes:
        print("Nenhuma transação realizada.")
    else:
        print("Histórico de transações:")
        for transacao in transacoes:
            print(transacao)

# Função de criar usuário
def criar_usuario(nome, cpf, endereco):
    usuario = {"nome": nome, "cpf": cpf, "endereco": endereco}
    return usuario

# Função de criar conta corrente
def criar_conta_corrente(usuario, numero_conta):
    conta_corrente = {"usuario": usuario, "numero_conta": numero_conta, "saldo": 0.0}
    return conta_corrente

while True:
    menu = '''
    [S] Para Saque
    [D] Para Depósito 
    [E] Para Extrato
    [C] Para Nova Conta
    [U] Para Novo Usuário
    [Q] Para Sair
    '''
    print(menu)

    escolha = str(input('Qual sua Escolha: ')).upper().strip()[0]

    if escolha == 'S':
        print(sacar())

    if escolha == 'D':
        print(depositar())

    if escolha == 'E':
        print(exibir_extrado())
    
    if escolha == 'Q':
        break