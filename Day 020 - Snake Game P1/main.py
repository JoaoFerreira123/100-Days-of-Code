from turtle import *
from snake import Snake
import time
from food import Food
from scoreBoard import Score

screen = Screen()

screen.setup(600, 600)
screen.bgcolor('gray') #muda a cor de fundo da tela
screen.title('Jogo da Cobrinha') #muda o texto na janela da tela
screen.tracer(0) #desliga as animações da tela


snake = Snake()
comida = Food()
pontuação = Score()

screen.listen()

#vai chamar os métodos que  mudam a direção da cobra quando pressionar as teclas
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


gameOn = True

while gameOn:
    screen.update() #atualiza a tela / liga novamente as animações
    # ao fazer isso, os 3 quadrados vão se mover com a tela "desligada",
    # só ligando a tela quando os 3 já tiverem movido, dando a impressão de que estão se movendo juntos
    time.sleep(0.1) #da a impressão de se mover mais devagar, dando uma pausa de 0.1s
    snake.move()
    

    #detectando a colisão da snake com comida
    if snake.head.distance(comida) < 15: #se a distância da cabeça da cobra até o objeto comida < 15
        comida.refresh()
        snake.extend()
        pontuação.comeu()
    
    #detectando colisão com a parede
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameOn = False
        pontuação.gameOver()

    #detectando colisão com o rabo
    #percorre a lista com os segmentos e verifica se a cabeça bateu em algum deles
    #verifica a distância entre a cabeça e cada segmento da cobra
    for i in snake.segmentos:
        if i != snake.head:
            if snake.head.distance(i) < 10:
                gameOn = False
                pontuação.gameOver()








screen.exitonclick()