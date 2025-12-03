def menu():
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Lista de contas
[q] Sair

=> """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito feito no valor de: R${valor}\n"
        print("Depósito realizado!")
    else:
        print("Não foi possível realiazer a transação, verifique o valor.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Transação cancelada, saldo insuficiente.")

    elif excedeu_limite:
        print("Transação cancelada, valor do saque excede o limite.")

    elif excedeu_saques:
        print("Transação cancelada, número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor}\n"
        numero_saques += 1
        print("Saque realizado.")

    else:
        print("Não foi possível realiazer a transação, verifique o valor.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("Não foi possivél completar a transação." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):

    cpf = input("Informe somente os números do CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado, informe um CPF válido:")
        return

    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereço = input("Informe o endereço (logradouro - Número - Bairro - Cidade/Uf):")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereço": endereço
    })

    print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o seu CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f""" 
Agência: {conta["agencia"]}
C/C: {conta["numero_conta"]}
Titular: {conta["usuario"]["nome"]}
"""
        print("=" * 100)
        print(linha)

def main():

    LIMITE_SAQUES = 4
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor para saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, tente novamente.")
            
main()
