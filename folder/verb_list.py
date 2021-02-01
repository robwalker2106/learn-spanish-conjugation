import pandas as pd
import turtle as Turtle


class Verbs:
    def __init__(self, data):
        self.data = data
        self.new_verbs = self.data[self.data.time_attempted == 0]
        self.good_verbs = self.data[self.data.precentage > 75]
        self.hard_verbs = self.data[self.data.precentage < 25]
        #self.weak_verbs = self.data[self.data.precentage >= 50 & self.data.precentage < 75]








