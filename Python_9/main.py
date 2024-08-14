from data import question_data
from question_model import  Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['answer']
    new_question = Question(question_text , question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.stil_has_question:
    quiz.next_question()


print("You've a completed the Quiz")
print(f"Your score is {quiz.score} / {len(question_bank)}")