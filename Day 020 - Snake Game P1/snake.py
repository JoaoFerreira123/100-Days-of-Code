from turtle import Turtle

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
moveDistance = 20

#Classe Snake, que a cada vez que é chamada, cria a cobra com a função createSnake, usando as posições 
#contidas em starting_pos

class Snake:
    def __init__(self):
        self.segmentos = []
        self.createSnake()
        self.head = self.segmentos[0] #cria um atributo, que é a direção.
        #Inicia ele como sendo o primeiro quadrado, que é a "cabeça" que guia a cobra
    
    def createSnake(self):
        for i in starting_pos:
            s = Turtle('square')
            s.penup()
            s.goto(i)
            self.segmentos.append(s)

    def move(self):
        #cada quadrado vai para a posição do quadrado anterior
        #dessa forma, a cobra conseque se mover e fazer curvas movendo só o primeiro quadrado, segmentos[0], ou, self.head
        for i in range(len(self.segmentos)-1, 0, -1):
            newX = self.segmentos[i - 1].xcor()
            newY = self.segmentos[i - 1].ycor()
            self.segmentos[i].goto(newX, newY)
        self.head.forward(moveDistance) #movendo o primeiro quadrado
    
    #métodos para mudarem a direção da head da cobra
    #os if's são pra garantir que ela não possa mudar para a direção oposta sem "fazer a volta" -> "não dar ré"
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
