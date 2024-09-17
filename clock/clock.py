class Clock:
    def __init__(self, hour, minute):
        self.hour = hour + minute // 60
        self.minute = minute % 60
        self.hour = self.hour % 24

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        total_minutes = self.minute + minutes
        return Clock(self.hour+total_minutes//60, total_minutes % 60)

    def __sub__(self, minutes):
        total_diff = self.minute - minutes
        return Clock(self.hour+total_diff//60, total_diff % 60)
