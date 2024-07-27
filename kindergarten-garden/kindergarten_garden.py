students_data = (
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
    'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry',
)

values = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}


class Garden:

    def __init__(self, diagram, students=students_data):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, name):
        index = self.students.index(name) * 2
        return [values[P[i]] for P in self.diagram for i in (index, index+1)]


