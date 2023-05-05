import random


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def has_questions(self):
        if len(self.question_list) > 0:
            return True
        else:
            return False

    def next_question(self):
        question = random.choice(self.question_list)
        self.question_number += 1
        user_reply = (input(f"\nQUES {self.question_number}: {question.question}? True/False ").lower())
        self.question_list.remove(question)
        return user_reply == question.answer.lower()

    def play_quiz_game(self):
        """
        Play Quiz Game
        :return: when all question has been answered
        """
        is_game_end = False

        while not is_game_end:

            if not self.has_questions():
                is_game_end = True
            else:
                if self.next_question():
                    self.score += 1
                    print(f"Your answer is correct, score {self.score}/{self.question_number}")
                else:
                    print(f"Your answer is incorrect, score {self.score}/{self.question_number}")

        print(f"\nYour final score was {self.score}/{self.question_number}")
