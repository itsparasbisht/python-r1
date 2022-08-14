question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __repr__(self):
        return f"Question('{self.text}', '{self.answer}')"

questions = []
print("------------------answer all the questions, you have 3 points---------------\n")
for i in question_data:
    questions.append(Question(i["text"], i["answer"]))

user_points = 3

for question in questions:
    print("->", question.text)
    user_response = input("True or False: \n")
    print("")
    if(user_response.lower() == question.answer.lower()):
        continue
    else:
        user_points -= 1

    if(user_points == 0):
        print("...........GAME OVER............")
        break
else:
    print("👏👏👏👏👏👏YOU WON👏👏👏👏👏👏")