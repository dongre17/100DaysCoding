import random


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def has_another_questions(self):
        if len(self.question_list) > 0:
            return True
        else:
            return False

    def next_question(self):
        question = random.choice(self.question_list)
        self.question_number += 1

        user_reply = bool(input(f"QUES {self.question_number}: {question.question}? True/False "))

        if user_reply == question.answer:
            self.score += 10
            print(f"Your answer is correct and your score {self.score}!!")
            self.question_list.remove(question)

            if self.has_another_questions():
                self.next_question()
            else:
                print("Wow you have answered all questions correctly...")

        else:
            print("Your answer is incorrect. Better luck next time..")
