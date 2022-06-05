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
    for i in range(len(alfabeto)):
        for j in range(len(msg)):
            if alfabeto[i] == msg[j]:
                if i-codigo	< 0:
                    pos = (i-codigo)+len(alfabeto)
                    desencripta.append(alfabeto[pos])
                else:
                    desencripta.append(alfabeto[i-codigo])
#da erro pra descodificar nos casos em que na codificação ele volta do Z pro A (linha 12)

print(''.join(encriptada))
print(''.join(desencripta))