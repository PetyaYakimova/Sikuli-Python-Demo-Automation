from pages.base_page import BasePage
from utils.image_utils import image


class NotepadPage(BasePage):

    def open_file_menu(self):
        self.screen.click(image("images/file_menu.png"))

    def click_save_as(self):
        self.screen.click("images/save_as.png")
