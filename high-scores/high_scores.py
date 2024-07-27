class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def scores(self, scores):
        return scores

    def latest(self):
        return self.scores[len(self.scores)-1]

    def personal_best(self):
        return sorted(self.scores)[len(self.scores)-1]

    def personal_top_three(self):
        return sorted(self.scores,reverse=True)[:3]