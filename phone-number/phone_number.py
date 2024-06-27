import re


class PhoneNumber:
    def __init__(self, phone_number):
        if re.search(r"[a-zA-Z]", phone_number):
            raise ValueError("letters not permitted")
        if re.search(r"[^0-9-().+ ]", phone_number):
            raise ValueError("punctuations not permitted")
        clean = "".join([x for x in phone_number if x.isdigit()])
        if len(clean) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(clean) == 11 and clean[0] != "1":
            raise ValueError("11 digits must start with 1")
        if len(clean) > 11:
            raise ValueError("must not be greater than 11 digits")
        self.clean = clean[1:] if len(clean) == 11 else clean
        if self.clean[0] == "0":
            raise ValueError("area code cannot start with zero")
        if self.clean[0] == "1":
            raise ValueError("area code cannot start with one")
        if self.clean[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if self.clean[3] == "1":
            raise ValueError("exchange code cannot start with one")

    @property
    def number(self):
        return self.clean

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        num = self.number
        return "(" + num[:3] + ")-" + num[3:6] + "-" + num[6:]
