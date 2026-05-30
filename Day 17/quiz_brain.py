class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
        self.user_answer = ''
    def next_question(self):

            current_question = self.questions_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
            self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's Wrong!")
        print(f"The correct answer was {current_answer}")
        print(f"Your current score is: {self.score}/{self.question_number} {"\n"* 2}")

    def still_has_questions(self):
        if (self.question_number - 5 == self.score):
            print("You got 5 wrong you lose!")
        else:
         quiz_length = len(self.questions_list)
         return quiz_length > self.question_number

