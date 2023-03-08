class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.students = []

    def rate_hw_lect(self, lecturer, course, rate_lecturer):
        if isinstance(lecturer, Lecturer) and course in lecturer.attached_courses and course in self.courses_in_progress:
            if course in lecturer.rates_lecturer:
                lecturer.rates_lecturer[course] += [rate_lecturer]
            else:
                lecturer.rates_lecturer[course] = [rate_lecturer]
        else:
            return 'Ошибка'

    def avg_grades(self):
        all_grades_courses = []
        if len(self.grades) > 0:
            for value in self.grades.values():
                all_grades_courses.extend(value)
            if len(all_grades_courses) > 0:
                average_grades = round(sum(all_grades_courses) / len(all_grades_courses), 1)
                return average_grades  # расчёт среднего балла
        return "No grades"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.avg_grades()}\n" \
               f"Курсы в процессе изучения: {('').join(self.courses_in_progress)}\nЗавершенные курсы: {('').join(self.finished_courses)}\n"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.attached_courses = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rates_lecturer = {}
        self.lecturers = []

    def avg_rate_lecturer(self):
        # функция для вычисления среднего балла
        all_rates = []
        if len(self.rates_lecturer) > 0:
            for value in self.rates_lecturer.values():
                all_rates.extend(value)
            if len(all_rates) > 0:
                rates_lecturer = round(sum(all_rates) / len(all_rates), 1)  # расчёт среднего балла
                return rates_lecturer
        return "No rates"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.avg_rate_lecturer()}\n"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.attached_courses and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


best_student = Student('Ruoy', 'Eman', 'men')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
best_student.grades['Python'] = [10, 10, 10, 10]

simple_student = Student('Jack', 'Black', 'men')
simple_student.courses_in_progress += ['Git']
simple_student.finished_courses += ['Основы Python']
simple_student.grades['Git'] = [8, 7, 8, 9, 10]

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.attached_courses += ['Python']

best_student.rate_hw_lect(cool_lecturer, 'Python', 10)
best_student.rate_hw_lect(cool_lecturer, 'Python', 9)
best_student.rate_hw_lect(cool_lecturer, 'Python', 9)
best_student.rate_hw_lect(cool_lecturer, 'Python', 10)

other_mentor = Reviewer('Sam', 'Smith')
other_mentor.attached_courses += ['Git']

print(best_student)
print(other_mentor)
print(cool_lecturer)
