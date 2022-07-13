from turtle import pen


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)#chamando a função check_answers

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        #vai retornar True ou False
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()[0] == correct_answer.lower()[0]:
            self.score += 1
            print('Correto!')
        else:
            print('Errado!')
        print(f'A resposta correta é {correct_answer}')
        print(f'Pontuação atual {self.score}/{self.question_number}')
        print('\n')
