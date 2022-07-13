class User:
    def __init__(self, user_id, username):
        print('Novo usuário sendo criado')
        #a função init é a construtora da classe, e vai se executada quando criar novos objetos
        self.id = user_id #o atributo é id, o user_id é só uma variável da função
        self.username = username #aqui o atributo e a variável tem o mesmo nome, o que é bem comum
        self.follwers = 0 
        self.following = 0
    
    def follow(self, user):
        user.follwers += 1
        self.following += 1

user_1 = User('001', 'João')
user_2 = User('002', 'Vitor')

user_1.follow(user_2)

print(user_1.follwers)
print(user_1.following)

print(user_2.follwers)
print(user_2.following)