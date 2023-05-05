class Question:
    """ Create a question model"""
    def __init__(self, question, answer):
        """ Constructor"""
        print(f"{question} {answer}")
        self.question = question
        self.answer = answer
