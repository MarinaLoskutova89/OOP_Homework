# Task
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
        and course in lecturer.courses_attached \
        and course in self.courses_in_progress and grade > 0 and grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def get_avg_grades(self):
        if self.grades:
            sum_hw = 0
            count = 0
            for grades in self.grades.values():
                sum_hw += sum(grades)
                count += len(grades)
            return round(sum_hw / count, 2)
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за домашние задания: {self.get_avg_grades()}\n'\
              f'Курсы в процессе изучения: {self.courses_in_progress}\n'\
              f'Завершенные курсы: {self.finished_courses}\n'
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Студента с такой фамилией нет!')
            return
        else:
            compare = self.get_avg_grades() < other_student.get_avg_grades()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{other_student.name} {other_student.surname} учится хуже, чем {self.name} {self.surname}')
        return compare

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.get_avg_lecture_grades()}\n'
        return res

    def get_avg_lecture_grades(self):
        if self.grades:
            res = round(sum(self.grades) / len(self.grades), 2)
            return res
        else:
            return 'Ошибка'

    def __lt__(self, other_lecture):
        if not isinstance(other_lecture, Lecturer):
            print('Лектора с такой фамилией нет!')
            return
        else:
            compare = self.get_avg_lecture_grades() < other_lecture.get_avg_lecture_grades()
            if compare:
                print(f'Лучший лектор: {other_lecture.name} {other_lecture.surname}')
            else:
                print(f'Лучший лектор: {self.name} {self.surname}')
        return compare

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
        and course in self.courses_attached \
        and course in student.courses_in_progress and grade > 0 and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'
        return res

natalia_vasina = Student('Natalia', 'Vasina', 'female')
natalia_vasina.finished_courses += ['Основы программирования']
natalia_vasina.finished_courses += ['Git']
natalia_vasina.courses_in_progress += ['Python']

dmitriy_kotikov = Student('Dmitriy', 'Kotikov', 'male')
dmitriy_kotikov.finished_courses = 'Основы программирования'
dmitriy_kotikov.courses_in_progress += ['Python']
dmitriy_kotikov.courses_in_progress += ['Git']

stanislav_korolev = Lecturer('Stanislav', 'Korolev')
stanislav_korolev.courses_attached += ['Python']

maksim_rodin = Lecturer('Maksim', 'Rodin')
maksim_rodin.courses_attached += ['Git']

vladislav_soroka = Reviewer('Vladislav', 'Soroka')
vladislav_soroka.courses_attached += ['Python']

anastasia_kukuruza = Reviewer('Anastasia', 'Kukuruza')
anastasia_kukuruza.courses_attached += ['Git']

vladislav_soroka.rate_hw(natalia_vasina, 'Python', 7)
vladislav_soroka.rate_hw(natalia_vasina, 'Python', 5)
vladislav_soroka.rate_hw(natalia_vasina, 'Python', 9)
vladislav_soroka.rate_hw(natalia_vasina, 'Python', 4)

anastasia_kukuruza.rate_hw(dmitriy_kotikov, 'Git', 8)
anastasia_kukuruza.rate_hw(dmitriy_kotikov, 'Git', 10)
vladislav_soroka.rate_hw(dmitriy_kotikov, 'Python', 7)
vladislav_soroka.rate_hw(dmitriy_kotikov, 'Python', 4)

dmitriy_kotikov.rate_lecturers(stanislav_korolev, 'Python', 4)
natalia_vasina.rate_lecturers(stanislav_korolev, 'Python', 9)

dmitriy_kotikov.rate_lecturers(maksim_rodin, 'Git', 7)
natalia_vasina.rate_lecturers(maksim_rodin, 'Git', 9)

print(natalia_vasina)
print(dmitriy_kotikov)
print(stanislav_korolev)
print(maksim_rodin)
print(vladislav_soroka)
print(anastasia_kukuruza)

print(natalia_vasina.grades)
print(dmitriy_kotikov.grades)
print(stanislav_korolev.grades)
print(maksim_rodin.grades)

print(natalia_vasina < dmitriy_kotikov)

print(stanislav_korolev < maksim_rodin)


def get_avg_hw_grade(student_list, course):
    total_sum = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)

def get_avg_lect_grade(list_lect):
    total_sum = 0
    for lecturer in list_lect:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
    return round(total_sum / len(list_lect), 2)

print(get_avg_hw_grade([natalia_vasina, dmitriy_kotikov], 'Python'))
print(get_avg_lect_grade([stanislav_korolev, maksim_rodin]))