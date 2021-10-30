from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    for text, answer in question.items():
        question_bank.append(Question(text, answer))

print(question_bank[0].answer)
