from curses.ascii import isdigit
IValue,ProductList,ClientDiscountPoints,CPF,CPFI,ClientPoints = [],[],[],[],[],[]
def validate_cpf(cpf):
    if len(cpf) != 11:
        return False    
    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    calc = [i for i in range(1, 10)]
    d1= (sum([int(a)*b for a,b in zip(cpf[:-2], calc)]) % 11) % 10
    d2= (sum([int(a)*b for a,b in zip(reversed(cpf[:-2]), calc)]) % 11) % 10
    return str(d1) == cpf[-2] and str(d2) == cpf[-1] 
while True:
    cpfRecebido = input("Cadastre seu CPF: ")
    if cpfRecebido in CPF: print('CPF já existente!')
    elif validate_cpf(cpfRecebido) == True: CPF.append(cpfRecebido), CPFI.append(cpfRecebido); print('CPF Cadastrado!')
    else: print('CPF Inválido!')
    Sign = int(input('Deseja cadastrar outro CPF? Sim[1] Não[2]\n'))
    if Sign == 2: ClientDiscountPoints = CPFI; break
while True:
    while True:
        ClientCPF = input('Para realizar a compra, digite seu CPF: ')
        if validate_cpf(ClientCPF) == True: break
        else: print('CPF Inválido!')
    isSigned = ClientCPF in CPF
    if isSigned: ClientI = CPF.index(ClientCPF)
    while True:
        ProductList.append(input('Insira o nome do produto a ser comprado:\n'))
        ProductValue = float(input('Insira o valor do produto:\nR$')); IValue.append(ProductValue)
        Choose = int(input("Mais produtos a comprar? Sim[1] Não[2]\n"))
        if Choose == 2: 
            ValueSum = sum(IValue)
            if isSigned: 
                for i in range(len(CPF)):
                    if CPF[i] == ClientCPF: 
                        if isdigit(ClientDiscountPoints[i]): ClientDiscountPoints[i] = ValueSum/5
                        else: ClientDiscountPoints[i] + ValueSum/5
            break
    if isSigned: 
        Choose = int(input('Deseja utilizar todos os seus pontos? Sim[1] Não [2]\n'))
        if Choose == 1: ValueSum -= (ClientDiscountPoints[ClientI] * 0.25); ClientDiscountPoints[ClientI] = 0
        print(f'CPF do cliente: {ClientCPF}\nQuantidade de pontos: {ClientDiscountPoints[ClientI]}\nTotal a pagar: {ValueSum}')
    else: print(f'Lista de compras: {ProductList}\nTotal a pagar: {ValueSum}')
    ValueSum = 0; IValue.clear(); ProductList.clear()
    Choose = int(input("Deseja fazer uma nova compra? Sim[1] Não[2]\n"))
    if Choose == 2: break