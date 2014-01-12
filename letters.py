class Letter:
    def __init__(self, letter_value):
        self.letter_value = letter_value
        self.min = 20.00
        self.max = 0.00
        self.cpt = 0

    def check_extrema(self, grade_value):

        if grade_value < self.min:
            self.min = grade_value
        if grade_value > self.max:
            self.max = grade_value
        if self.min > self.max:
            self.min,self.max = self.max,self.min