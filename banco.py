def deposito(saldo, valor, extrato):
    if(valor > 0):
        saldo += valor
        deposito_info = f"Foram depositados R$ {valor}\n"
        extrato += deposito_info
        print(deposito_info)
        print("".center(41,"="))  
    else:
        print("Valor inválido para deposito, caso queira desistir do deposito digite 0\n")
    return saldo, extrato, False

def saque(*,saldo, valor, extrato, limite, numero_saques, limites_saques):

    if(numero_saques < limites_saques):
        if(valor > 0):

            if(saldo >= valor and limite >= valor):
                saldo -= valor
                saque_info = f"Foram sacados R$ {valor}\n"
                extrato += saque_info
                numero_saques += 1
                print(saque_info + f"Você fez {numero_saques} de {limites_saques} saques diários\n")
                print("".center(41,"="))
                return saldo, extrato, numero_saques, False
            
            elif(saldo < valor):
                print(f"Saldo da conta insuficiente para o valor do saque, você possui R$ {saldo} na conta")

            elif(limite < valor):
                print(f"O valor do saque é maior que o limite, o limite é de R$ {limite}")

            print("Caso queira desistir do saque, digite 0\n")
            return saldo, extrato, numero_saques, True    
        
        elif(valor == 0):
            print("O valor digitado foi 0, sua operação de saque foi cancelada\n")
            print("".center(41,"="))
            return saldo, extrato, numero_saques, False
        
        else:
            print("Valor de saque inválido, por favor colocar um valor válido\nCaso queira desistir do saque, digite 0")

    else:
        print("\nVocê atingiu seu limite diário de saques\n")
        print("".center(41,"="))
        return saldo, extrato, numero_saques, False

def exibir_extrato(saldo, /, *, extrato):
    
    extrato_print = "\nNão foram realizadas movimentações" if(extrato == "")  else f"\n{extrato}"
    print(extrato_print)
    print(f"Você possui R${saldo} na conta\n")
    print("".center(41,"="))

def confirmar_conta(cpf, usuarios):
    matched_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return matched_usuario[0] if matched_usuario else None

def novo_usuario(usuarios):
    
    while True:
        cpf = input("\nDigite o seu CPF ou digite 0 para sair da operação\n")

        if cpf == 0:
            break
        usuario = confirmar_conta(cpf, usuarios)

        if usuario:
            print(f"\nEsse CPF já está cadastrado no sistema, saia da operação ou digite outro CPF\n")

        else:
            nome = input("Digite seu nome completo\n")
            data_nasc = input("Digite sua data de nascimento (dd-mm-yyyy)\n")
            endereco = input("Digite seu endereco (logradouro, nro, bairro - cidade/sigla - estado)\n")
            usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf":cpf, "endereco": endereco})
            print("Usuario criada com sucesso!".center(41,"="))
            break

def nova_conta(agencia, num_conta, usuarios):
    while True:
        cpf = input("\nDigite seu CPF ou digite 0 para sair da operação\n")
        
        if cpf == 0:
            return
        usuario = confirmar_conta(cpf, usuarios)

        if usuario:
            print("Conta criada com sucesso!")
            return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}
        
        print("\nUsuario não encontrado, tente novamente ou saia da operação\n")

def listar_contas(contas):
    for conta in contas:
        print("".center(41, "-"))
        print(f"Agência: {conta["agencia"]}")
        print(f"Numero da Conta: {conta["num_conta"]}")
        print(f"CPF do usuário: {conta["usuario"]["cpf"]}")
        print(f"Nome do usuário: {conta["usuario"]["nome"]}")
        print("".center(41, "-"))
    
def main():
    
    menu = """

        [d] Depositar
        [s] Sacar
        [e] Estrato
        [nu] Novo usuario
        [nc] Nova conta
        [lc] Listar contas
        [q] Sair

        => """
    
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    
    check = True
    
    usuarios = []
    contas = []


    while True:

        opcao = input(menu)

        if opcao == "d":
            check = True
            while check:
                print("Deposito".center(41,"="))
                deposito_input = float(input(f"\nInforme o valor a ser depositado: \n"))

                if(deposito_input == 0):
                    print("Valor digitado foi 0, logo a operação de depósito foi cancelada")
                    break

                else:
                    saldo, extrato, check = deposito(saldo, deposito_input, extrato)


        elif opcao == "s":
            print("Saque".center(41, "="))
            check = True
            while check:
                saque_input = float(input(f"\nInforme o valor a ser sacado,\no máximo possível por saque é de R$ {limite}:\n"))
                saldo, extrato, numero_saques, check = saque(
                    saldo=saldo,
                    valor=saque_input,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limites_saques=LIMITE_SAQUES
                )

        elif opcao == "e":
            print("Extrato".center(41, "="))
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            print("Novo usuário".center(41, "="))
            novo_usuario(usuarios)

        elif opcao == "nc":
            print("Nova Conta".center(41, "="))
            num_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, num_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            print("Listar Contas".center(41, "="))
            listar_contas(contas)
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()