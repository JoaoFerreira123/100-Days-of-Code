from functions import *

resources = {'Water':500, 'Coffee':76, 'Milk':500, 'money':2.5}
recipe = {'espresso':{'Water':50, 'Coffee':18}, 'latte':{'Water':200, 'Coffee':24, 'Milk':150}, 'cappuccino':{'Water':250, 'Coffee':24, 'Milk':100}}

while True:
    choice = menu()
    if choice == 'off':
        break
    elif choice == 'report':
        report(resources)
    else:    
        checkResources(choice, resources, recipe)
        money(choice, resources)

#funciona porém está MAL OTIMIZADO, muita coisa repetida
#solução otimizada: https://replit.com/@appbrewery/coffee-machine-final#main.py
#Testar outra versão melhor!!