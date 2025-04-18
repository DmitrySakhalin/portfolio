class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        if total_grades:
            return sum(total_grades) / len(total_grades)
        else:
            return 0

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Нельзя сравнивать студентов с другими объектами")
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Нельзя сравнивать студентов с другими объектами")
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Нельзя сравнивать студентов с другими объектами")
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        if total_grades:
            return sum(total_grades) / len(total_grades)
        else:
            return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Нельзя сравнивать лекторов с другими объектами")
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Нельзя сравнивать лекторов с другими объектами")
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Нельзя сравнивать лекторов с другими объектами")
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

print(some_student.grades)

some_student.rate_lecturer(some_lecturer, 'Python', 9)
some_student.rate_lecturer(some_lecturer, 'Python', 8)
some_student.rate_lecturer(some_lecturer, 'Python', 7)

print(some_lecturer.grades)

print(some_reviewer)
print(some_lecturer)
print(some_student)



another_student = Student('Some', 'Student', 'male')
another_student.courses_in_progress += ['Python']
some_reviewer.rate_hw(another_student, 'Python', 9)
some_reviewer.rate_hw(another_student, 'Python', 9)
some_reviewer.rate_hw(another_student, 'Python', 9)

another_lecturer = Lecturer('Some', 'Lecturer')
another_lecturer.courses_attached += ['Python']
some_student.rate_lecturer(another_lecturer, 'Python', 10)
some_student.rate_lecturer(another_lecturer, 'Python', 10)
some_student.rate_lecturer(another_lecturer, 'Python', 10)