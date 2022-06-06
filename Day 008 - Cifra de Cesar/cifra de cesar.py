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
                if i+codigo > len(alfabeto)-1:
                    encriptada.append(alfabeto[(i+codigo)-len(alfabeto)])
                else:
                    encriptada.append(alfabeto[i+codigo])

if opcao == 2:
    for i in range(len(msg)):
        for j in range(len(alfabeto)):
            if msg[i] == alfabeto[j]:
                if j-codigo	< 0: 
                    pos = (j-codigo)+len(alfabeto)
                    desencripta.append(alfabeto[pos])
                else:
                    desencripta.append(alfabeto[j-codigo])

print(''.join(encriptada))
print(''.join(desencripta))