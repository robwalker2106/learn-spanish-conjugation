from turtle import Turtle

SUBTITLES = {'yo': (-315, 190), 'tu': (-315, 47), 'el/ella/usted': (-315,  -90), 'nosotros': (15, 190),
             'vosotros': (15, 47), 'ellos/ellas/ustedes': (15, -90)}

FONT = ('Arial', 15, 'normal')

class SheetWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor('black')
        self.speed('fastest')
        self.hideturtle()

        for pronoun, coor in SUBTITLES.items():
            self.goto(coor)
            self.write(pronoun, move=True, align='left', font=FONT)


