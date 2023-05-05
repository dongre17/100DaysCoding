import random
class QuizBrain:

    def __init__(self, question_number, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        question = random.choice(self.question_list)
        user_reply = bool(input(f"QUES {self.question_number}: {question.question}? True/False "))

        if user_reply == question.answer:
            print("Your answer is correct !!")
            self.question_number += 1
            self.question_list.remove(question)
            self.next_question()
        else:
            print("Your answer is incorrect. Better luck next time..")




