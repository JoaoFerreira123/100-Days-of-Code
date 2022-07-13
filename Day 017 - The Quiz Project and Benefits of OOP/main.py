from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    q = Question(i['text'],i['answer'])
    question_bank.append(q)
    # pega a lista de questões de data.py, transforma em objetos de questões da classe Question
    # e coloca todos os objetos em uma lista
#print(question_bank)

#print(question_bank[0].answer) #answer do objeto da posição 0 da lista

quiz = QuizBrain(question_bank) #aqui ele já cria o quiz e passa a lista com as questões

while quiz.still_has_questions():
    quiz.next_question()
print(f'A sua pontuação final foi: {quiz.score}/{len(question_bank)}')