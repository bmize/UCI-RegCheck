# Class representing the basic characteristics of a course


class Course:
    def __init__(self, course_code, students_max):
        self.__course_code = course_code
        self.__students_max = students_max

    def set_course_code(self, course_code: int):
        self.__course_code = course_code

    def set_students_max(self, students_max: int):
        self.__students_max = students_max

    def get_course_code(self) -> int:
        return self.__course_code

    def get_students_max(self) -> int:
        return self.__students_max
