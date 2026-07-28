from pages.notepad_page import NotepadPage
from utils.logger import logger


def test_open_file_menu():
    page = NotepadPage()

    logger.info("Opening File menu")
    input("Open Notepad and press Enter...")

    page.open_file_menu()
