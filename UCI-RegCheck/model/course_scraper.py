"""course_scraper.py

Contains the CourseScraper class. This is to be used for gathering information
about a given course from the UCI class website, such as max and current
student enrollment counts.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from model.course import Course


class CourseScraper:
    """Uses Selenium and a headless browser (PhantomJS) to scrape the UCI class
    website for enrollment info.

    Attributes:
        _currently_enrolled_xpath: str representing the xpath location of the
            webpage table entry containing the number of currently enrolled
            students
        _max_enrolled_xpath: str representing the xpath location of the
            webpage table entry containing the max number of enrolled students
        delay_in_seconds: int that determines the intended delay between
            re-scraping the webpage for current enrollment info
    """
    BASE_URL = 'https://www.reg.uci.edu/perl/WebSoc'

    def __init__(self):
        self._currently_enrolled_xpath = '//td[10]'
        self._max_enrolled_xpath = '//td[9]'
        self.delay_in_seconds = 600

    def is_course_available(self, driver: webdriver.PhantomJS(), course: Course) -> bool:
        """
        :param driver: webdriver used for scraping the UCI enrollment webpage
        :param course: Course object used to store information about a course
        :return: True if a course is available, otherwise False
        """
        # TODO: double check and test function content
        driver.get(self.BASE_URL)
        assert "Schedule of Classes" in driver.title

        cc_elem = driver.find_element_by_name("CourseCodes")
        cc_elem.clear()
        cc_elem.send_keys(course.course_code)
        cc_elem.send_keys(Keys.RETURN)

        course.students_current = driver.find_element_by_xpath(self._currently_enrolled_xpath).text
        course.students_max = driver.find_element_by_xpath(self._max_enrolled_xpath).text

        return True if course.students_current < course.students_max else False
