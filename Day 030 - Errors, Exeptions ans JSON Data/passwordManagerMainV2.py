from tkinter import *
from tkinter import messagebox
import userInterfaceV2
import random
import pyperclip
import json

#Código 100% funcional porém USANDO JSON para a gravação dos arquivos 

def save():

    site = userInterfaceV2.website.get()
    email = userInterfaceV2.username.get()
    senha = userInterfaceV2.password.get()

    novosDados = {
        site: {
            'email': email,
            'password': senha
        }
    }

    if len(site) == 0 or len(email) == 0 or len(senha) == 0:
        messagebox.showerror(title='Erro', message='Não deixe Nenhum Campo em Branco')
    else:
        ok = messagebox.askokcancel(title=site, message=f'Confirme os Dados de Login:\nEmail: {email}\nPassword: {senha}')
        if ok:
                try:
                    with open('Day 030 - Errors, Exeptions ans JSON Data/dados.json', 'r') as arquivo:
                        dados = json.load(arquivo) #lendo os dados antigos
                except FileNotFoundError:
                    with open('Day 030 - Errors, Exeptions ans JSON Data/dados.json', 'w') as arquivo:
                        json.dump(novosDados, arquivo, indent=4)
                else:
                    dados.update(novosDados) #atualizando os dados

                    with open('Day 030 - Errors, Exeptions ans JSON Data/dados.json', 'w') as arquivo:
                        json.dump(dados, arquivo, indent=4) #gravando os dados
                
                finally:
                    userInterfaceV2.website.delete(0, 'end')
                    userInterfaceV2.username.delete(0, 'end')
                    userInterfaceV2.password.delete(0, 'end')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generatePassword():

    passwordLetters = [random.choice(letters) for i in range(random.randint(3, 6))]
    passwordSymbols = [random.choice(symbols) for i in range(random.randint(3, 6))]
    passwordNummbers = [random.choice(numbers) for i in range(random.randint(3, 6))]
    
    passwordList = passwordLetters + passwordSymbols + passwordNummbers
    random.shuffle(passwordList)

    senhaGerada = ''.join(passwordList)

    userInterfaceV2.password.insert(0, senhaGerada)
    pyperclip.copy(senhaGerada) #Copia a senha para o clipboard

def search():
    site = userInterfaceV2.website.get()
    try:
        with open('Day 030 - Errors, Exeptions ans JSON Data/dados.json', 'r') as arquivo:
            dados = json.load(arquivo)
            resultado = dados[site]

    except FileNotFoundError:
        messagebox.showerror(title='Erro', message='Arquivo de dados não encontrado')   
    except KeyError:     
            messagebox.showerror(title='Erro', message='Site não cadastrado')
    else:
        messagebox.showinfo(title=site, message=f"Email: {resultado['email']}\nSenha: {resultado['password']}")