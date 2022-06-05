alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

opcao = int(input('Quer ENCRIPTAR(1) ou DESENCRIPTAR?(2) '))
codigo = int(input('Qual o código? '))
msg = input('Digite a mensagem: ').lower()
encriptada = []
desencripta = []
if opcao == 1:
    for i in range(len(alfabeto)):
        for j in range(len(msg)):
            if alfabeto[i] == msg[j]:
                encriptada.append(alfabeto[i+codigo])
#Se i+código > len(alfabeto) ele buga. até encripta, mas da ruim pra desencriptar
if opcao == 2:
    for i in range(len(alfabeto)):
        for j in range(len(msg)):
            if alfabeto[i] == msg[j]:
                desencripta.append(alfabeto[i-codigo])

print(''.join(encriptada))
print(''.join(desencripta))