class Allergies:

    def __init__(self, score):
        self.allergens = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
        self.allergens = [self.allergens[i] for i in range(len(self.allergens)) if score & (1 << i)]

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        return self.allergens
