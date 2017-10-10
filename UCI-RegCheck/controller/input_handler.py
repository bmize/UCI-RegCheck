# input.py
from model import course_scraper
from view import menu


class InputHandler:
    def __init__(self):
        # self._input = None
        self._command_list = {'1', '2', '3'}
        self._course_scraper = course_scraper.CourseScraper()


    def receive_input(self):
        menu.display_welcome_message()

        while True:
            menu.display_main_menu(self._course_scraper.delay_in_seconds)
            user_input = input()


    def handle_input(self) -> None:
        # handle input
        return None
