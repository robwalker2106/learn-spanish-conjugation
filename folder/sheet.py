from turtle import Turtle

SUBHEADINGS = {'yo': (-315, 190), 'tú': (-315, 45), 'él/ella/usted': (-315, -92), 'nosotros': (15, 190),
             'vosotros': (15, 45), 'ellos/ellas/ustedes': (15, -92)}
ANSWERS = {'yo': (-190.0, 131.0), 'tú': (-190, 2), 'él/ella/usted': (-190,  -137), 'nosotros': (157.0, 131.0),
             'vosotros': (157, 2), 'ellos/ellas/ustedes': (157, -137)}

FONT = ('Arial', 15, 'normal')
ANSWERS_FONT = ('Arial', 30, 'normal')


class SheetWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor('black')
        self.speed('fastest')
        self.hideturtle()
        self.subheadings()

    def subheadings(self):
        for pronoun, coor in SUBHEADINGS.items():
            self.pencolor('black')
            self.goto(coor)
            self.write(pronoun, move=True, align='left', font=FONT)

    def print_answer(self, pronoun, answer, correct):
        coor = ANSWERS[pronoun]
        self.pencolor('red3')
        if correct == 'correct':
            self.pencolor('green3')
        self.penup()
        self.goto(coor)
        self.write(answer, move=True, align='center', font=ANSWERS_FONT)

    def clear_answers(self):
        self.clear()
        self.subheadings()






