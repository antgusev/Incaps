class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n'\
            f'Фамилия: {self.surname}\n'\
                f'Средняя оценка за домашние задания: {self._rate_hw()}\n'\
                    f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
                        f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def _rate_hw(self):
        sum_ = 0
        count = 0
        for course in self.grades.values():
            sum_ += sum(course)
            count += len(course)
        return round(sum_ / count, 2)
    
        #средняя оценка за домашние задания по всем студентам в рамках конкретного курса
    def get_avg_stud_grade(students, course):
        sum_ = 0
        for student in students:
            sum_ += sum(student.grades[course]) / len(student.grades[course])

        return sum_ / len(students)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    # def __init__(self, name, surname):
    #    super().__init__(name, surname)
    #    self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n'f'Средняя оценка за лекции: {self._get_average_grade()}'
    
    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Ошибка')
            return
        else:
            compare = self._get_average_grade() < other_lecturer._get_average_grade()

        if compare:
            print(f'У {self.name} {self.surname} оценка хуже чем, у {other_lecturer.name} {other_lecturer.surname}')
        else:
            print(f'У {self.name} {self.surname} оценка лучше чем, у {other_lecturer.name} {other_lecturer.surname}')
    
    def _get_average_grade(self):
        sum_ = 0
        count = 0
        for course in self.grades.values():
            sum_ += sum(course)
            count += len(course)
        return round(sum_ / count, 2)
    
    #средняя оценка за лекции всех лекторов в рамках курса
    def get_avg_lect_grade(lecturers, course):
        sum_ = 0
        for lecturer in lecturers:
            sum_ += sum(lecturer.grades[course]) / len(lecturer.grades[course])

        return sum_ / len(lecturers)


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}'
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in self.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# best_student.courses_in_progress += ['Git']
# best_student.rate_lecturer(oleg_bulygin, 'Python', 5)
# best_student.rate_lecturer(oleg_bulygin, 'Python', 4)
# best_student.rate_lecturer(oleg_bulygin, 'Git', 5)

# print(get_avg_lect_grade([oleg_bulygin], 'Python'))
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 

#Студенты

elena_guseva = Student('Elena', 'Guseva', 'female')
elena_guseva.courses_in_progress += ['Python']
elena_guseva.courses_in_progress += ['Git']
elena_guseva.rate_lecturer(lecturer2, 'Python', 5)
elena_guseva.rate_lecturer(lecturer2, 'Python', 4)
elena_guseva.rate_lecturer(lecturer2, 'Git', 5)


ksenya_guseva = Student('Ksenya', 'Guseva', 'female')
ksenya_guseva.courses_in_progress += ['Python'] 
ksenya_guseva.courses_in_progress += ['C++']
ksenya_guseva.rate_lecturer(lecturer1, 'Python', 5)
ksenya_guseva.rate_lecturer(lecturer1, 'Python', 4)
ksenya_guseva.rate_lecturer(lecturer1, 'Git', 5)


# print (ksenya_guseva)


#Лекторы

lecturer1 = Lecturer('Oleg', 'Bulygin')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']

lecturer2 = Lecturer('Elena', 'Nikitina')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']


#Проверяющие

aleksander_bardin = Reviewer('Aleksander', 'Bardin')
aleksander_bardin.courses_attached += ['Python']
aleksander_bardin.courses_attached += ['C++']

denis_rudakov = Reviewer('Denis', 'Rudakov')
denis_rudakov.courses_attached += ['Python']
denis_rudakov.courses_attached += ['C++']

#print(aleksander_bardin)
