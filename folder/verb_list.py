from turtle import Turtle
from random import choice

FONT = ('Arial', 30, 'normal')
TITLE_POSITION = (-3, 235)
INGLES_POSITION = (-3, 210)


class Verbs:
    def __init__(self, data, csv, amount):
        self.data = data
        self.csv = csv
        self.amount = amount
        self.verb_tense_pf = self.data
        self.create_list()
        # TODO: Turn this into a dictionary
        self.list_of_verbs = self.verb_tense_pf.values.tolist()
        self.attempts = 0
        self.correct = 0
        print(self.list_of_verbs)

    def create_list(self):
        weak_verbs_pd = self.data[self.data.percentage <= .50]
        print(len(weak_verbs_pd))
        if len(weak_verbs_pd) < self.amount:
            weak_verbs_pd = self.data[self.data.percentage <= .75]
        if len(weak_verbs_pd) < self.amount:
            self.verb_tense_pf = self.data[['infinitive', 'tense']]
        else:
            self.verb_tense_pf = weak_verbs_pd[['infinitive', 'tense']]

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
        self.data.to_csv(self.csv, encoding='mac_roman', index=False)











