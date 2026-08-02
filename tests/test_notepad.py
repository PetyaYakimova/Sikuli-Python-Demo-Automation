import subprocess
import time

from pages.notepad_page import NotepadPage
from utils.logger import logger


def test_open_file_menu(notepad):
    page = NotepadPage()

    page.open_file_menu()
