from lackey import Screen


class NotepadPage:

    def __init__(self):
        self.screen = Screen()

    def open_file_menu(self):
        self.screen.click("images/file_menu.png")

    def click_save_as(self):
        self.screen.click("images/save_as.png")