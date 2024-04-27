class Luhn:

    def __init__(self, card_num):
        self.card_value = card_num

    def valid(self):
        self.card_value = self.card_value.replace(" ", "")
        if self.card_value.isdigit() and len(self.card_value) > 1:
            sum_value = 0
            for i in range(len(self.card_value)):
                digit = int(self.card_value[i])
                if i % 2 == len(self.card_value) % 2:
                    digit *= 2
                if digit > 9:
                    digit -= 9
                sum_value += digit
            if sum_value % 10 == 0:
                return True
            else:
                return False
        else:
            return False
