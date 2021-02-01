import pandas as pd
from turtle import Turtle
from random import choice

FONT = ('Arial', 30, 'normal')
TITLE_POSITION = (-3, 235)
INGLES_POSITION = (-3, 210)

class Verbs:
    def __init__(self, data):
        self.data = data
        self.new_verbs = self.data[self.data.time_attempted == 0]
        self.good_verbs = self.data[self.data.precentage > 75]
        self.hard_verbs = self.data[self.data.precentage < 25]
        self.verb_tense_pf = self.data[['infinitive', 'tense']]
        self.list_of_verbs = self.verb_tense_pf.values.tolist()
        self.attempts = 0
        self.correct = 0

    def verb_challenge(self):
        verb = Turtle()
        verb.hideturtle()
        verb.penup()
        verb.goto(TITLE_POSITION)
        infinitive, tense = choice(self.list_of_verbs)
        index = self.data.index[(self.data.infinitive == infinitive) & (self.data.tense == tense)]
        verb_row = self.data[(self.data.infinitive == infinitive) & (self.data.tense == tense)]
        ingles = verb_row.iloc[0]['ingles']
        self.attempts = verb_row.time_attempted
        self.correct = verb_row.times_correct
        verb.write(infinitive + "    :    " + tense, move=True, align='center', font=FONT)
        verb.goto(INGLES_POSITION)
        verb.write(ingles, move=True, align='center', font=FONT)
        return verb_row, index

    def updated_verb_info(self, index, correct):
        self.attempts += 1
        self.data.at[index, 'time_attempted'] = self.attempts

        if correct:
            self.correct += 1
            self.data.at[index, 'times_correct'] = self.correct

        self.data.at[index, 'percentage'] = self.correct / self.attempts
        self.data.to_csv('verbs.csv', encoding='mac_roman', index=False)











