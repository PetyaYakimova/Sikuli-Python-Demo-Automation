from pages.base_page import BasePage


class NotepadPage(BasePage):

    def open_file_menu(self):
        self.screen.click("images/file_menu.png")

    def click_save_as(self):
        self.screen.click("images/save_as.png")