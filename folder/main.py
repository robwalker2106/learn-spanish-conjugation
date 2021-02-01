from turtle import Turtle, Screen
import pandas as pd
from verb_list import Verbs
from sheet import SheetWriter

screen = Screen()
image = 'sheet.gif'
screen.addshape(image)
screen.title("Spanish Verb Conjugation")
screen.screensize(canvwidth=800, canvheight=800)
screen.setup(width=900, height=900)
sheet = Turtle(image)
screen.tracer(0)
sheet_writer = SheetWriter()
screen.update()
verbs = Verbs(pd.read_csv('verbs.csv'))


screen.mainloop()