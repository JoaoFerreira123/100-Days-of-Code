

def menu():
    print('O que gostaria?')
    print("""
            1 - Espresso
            2 - Latte
            3 - Cappuccino""")
    choice = int(input(''))
    return choice

def report(resources):
    for tipo in resources:
        print(f'{tipo}: {resources[tipo]}')
    
def checkResources(choice, resources, recipe):
    #tentei fazer de forma "automatica" com for, mas não consegui -> tentar dnv depois
    if choice == 1:
        if(resources['Water'] >= recipe['espresso']['Water'] and resources['Coffee'] >= recipe['espresso']['Coffee']):
            resources['Water'] -= recipe['espresso']['Water']
            resources['Coffee'] -= recipe['espresso']['Coffee']
        else:
            print('Sem ingredientes o suficiente')
    elif choice == 2:
        if(resources['Water'] >= recipe['latte']['Water'] and resources['Coffee'] >= recipe['latte']['Coffee'] and resources['Milk'] >= recipe['latte']['Milk']):
            resources['Water'] -= recipe['latte']['Water']
            resources['Coffee'] -= recipe['latte']['Coffee']
            resources['Milk'] -= recipe['latte']['Milk']
        else:
            print('Sem ingredientes o suficiente')
    elif choice == 3:
        if(resources['Water'] >= recipe['cappuccino']['Water'] and resources['Coffee'] >= recipe['cappuccino']['Coffee'] and resources['Milk'] >= recipe['cappuccino']['Milk']):
            resources['Water'] -= recipe['cappuccino']['Water']
            resources['Coffee'] -= recipe['cappuccino']['Coffee']
            resources['Milk'] -= recipe['cappuccino']['Milk']
        else:
            print('Sem ingredientes o suficiente')
    else: 
        print('Por favor escolha uma opção existente')

def money(choice, resources):
    if choice == 1:
        print('O espresso custa $1.5')
        cash = float(input('Coloque o dinheiro: '))
        if cash < 1.5:
            print('Dinheiro insuficiente')
            return
        change = cash - 1.5 
        resources['money'] += cash-change
        print(f'Retire o troco de R$: {change}')
    
        
