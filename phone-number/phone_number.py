class PhoneNumber:
    def __init__(self, number):
        self.number = number
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(self.number) > 11 and self.number[0] != 1:
            raise ValueError("11 digits must start with 1")
        elif len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
        else:
            print("not value ")
        


