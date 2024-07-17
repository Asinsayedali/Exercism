
class School:
    def __init__(self):
        self.students_data = {}
        self.status_update = []

    def add_student(self, name, grade):
        if name in self.students_data.keys():
            self.status_update.append(False)
        else:
            self.students_data[name] = grade
            self.status_update.append(True)


    def roster(self):
        sorted_list = sorted(self.students_data.items(), key = lambda item: (item[1], item[0]))
        return [name for name, grade in sorted_list]

    def grade(self, grade_number):
        list_students = []
        for key, value in self.students_data.items():
            if value == grade_number:
                list_students.append(key)
        return sorted(list_students)



    def added(self):
        return self.status_update
