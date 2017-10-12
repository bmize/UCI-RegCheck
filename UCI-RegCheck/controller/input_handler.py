"""input_handler.py

Contains the InputHandler class and methods used for interpreting user input
and calling the appropriate function/method.
"""

from model.course_scraper import CourseScraper
from view import menu


class InputHandler:
    """Contains methods to read and handle user input.

    Attributes
        _commands: Set of integers corresponding to the numbers in
            view.menu.display_main_menu()
        _course_scraper: CourseScraper object used for gathering and
            sharing course information.
    """

    def __init__(self):
        self._commands = {'1', '2', '3'}
        self._course_scraper = CourseScraper()

    def receive_input(self):
        """Primary loop for continuously receiving user input until program is
        exited.

        :return: None
        """
        menu.display_welcome_message()

        while True:
            menu.display_main_menu(self._course_scraper.delay_in_seconds)
            user_input = input()
            self.handle_input(user_input)

    def handle_input(self, user_input: str):
        """Calls appropriate function/method depending on user_input. Uses
        self._commands to tie user_input to menu options in
        view.menu.display_main_menu()

        :param user_input: str correlating to menu options in
            view.menu.display_main_menu()
        :return: None
        """
        # TODO: check user_input and perform appropriate action
