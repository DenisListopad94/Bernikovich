class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.exams = []
        self.marks = []

    def registration(self):
        print(f"Adding {self.name} {self.surname} to student list")

    def add_exam_result(self, exam_name, mark):
        self.exams.append(exam_name)
        self.marks.append(mark)


class Faculty:
    def __init__(self, name_faculty):
        self.name_faculty = name_faculty
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)
        print(f"Added {student.name} {student.surname} to faculty: {self.name_faculty}")


class Exam:
    @staticmethod
    def record_marks(exam_name, teacher_name, marks):
        print(f"Exam: {exam_name}, Teacher: {teacher_name}, Marks: {marks}")


class Teacher:
    @staticmethod
    def give_rating(teacher_name, surname, marks):
        pass  # Add functionality for giving ratings


class EnrollmentSystem:
    @staticmethod
    def count(average_score, enrolled_students):
        print(f"Average score: {average_score}")
        print(f"Enrolled students: {enrolled_students}")