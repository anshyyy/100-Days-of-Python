from question_model import Question
from data import question_data
from quiz_brain import Quiz
question_bank = []
for ques in question_data:
    question_text = ques["question"]
    question_ans = ques["correct_answer"]
    new_ques = Question(question_text, question_ans)
    question_bank.append(new_ques)

quiz = Quiz(question_bank)
while quiz.still_has_question():
       quiz.next_ques()

quiz.cong()


