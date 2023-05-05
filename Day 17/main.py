from question import Question
from questions_data import question_data
from quiz_brain import QuizBrain

question_bank = []

for key in question_data:
    question = key['question']
    answer = key['answer']
    question_bank.append(Question(question, answer))

quiz = QuizBrain(question_bank)

quiz.next_question()

