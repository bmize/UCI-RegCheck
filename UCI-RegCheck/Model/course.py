"""course.py

Contains the Course class which is used to represent the basic characteristics
 of a UCI course
"""


class Course:
    """Represents a Course object"""

    def __init__(self, course_code):
        """
        :param course_code: int representing a specific course offered by
         UCI. For example, 36595 in the Fall Quarter of 2017 represents the
         course ICS 31.
        :param students_current: int representing the current number of
         students enrolled in this course
        :param students_max: int representing the maximum number of
         students enrolled in this course
        """
        self.course_code = course_code
        self.students_current = None
        self.students_max = None
