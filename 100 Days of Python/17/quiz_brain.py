class Quiz:
    def __init__(self, ques_list):
        self.ques_no = 0
        self.question_list = ques_list
        self.score= 0

    def next_ques(self):
        curr_ques = self.question_list[self.ques_no]
        self.ques_no += 1
        user_ans = input(f"Q.{self.ques_no}: {curr_ques.text} (True/False) ")
        self.check_ans(user_ans, curr_ques.answer)

    def still_has_question(self):
        return self.ques_no < len(self.question_list)

    def check_ans(self, user_answer, curr_ans):
        if user_answer.lower() == curr_ans.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's Wrong")
        print(f"The correct Answer was : {curr_ans}")
        print(f"Your current Score is : {self.score}/{self.ques_no}\n")

    def cong(self):
        if self.score > self.ques_no//2 :
            print(f"Congratulations ! your final score is {self.score}/{self.ques_no}")
        else:
            print(f"Its okay... Try again!! "
                  f"Your score was : {self.score}/{self.ques_no}")


