# Class representing the basic characteristics of a course


class Course:
    def __init__(self, course_code, students_max):
        self._course_code = course_code
        self._students_max = students_max

    def set_course_code(self, course_code: int):
        self._course_code = course_code

    def set_students_max(self, students_max: int):
        self._students_max = students_max

    def get_course_code(self) -> int:
        return self._course_code

    def get_students_max(self) -> int:
        return self._students_max
