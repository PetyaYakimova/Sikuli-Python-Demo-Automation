from pages.notepad_page import NotepadPage
from utils.logger import logger


def test_open_file_menu():
    page = NotepadPage()

    logger.info("Opening File menu")
    input("Open Notepad and press Enter...")

    page.open_file_menu()


#import subprocess
#import time

#from pages.notepad_page import NotepadPage
#from utils.logger import logger


#def test_open_file_menu():
    #logger.info("Starting Notepad")

    #subprocess.Popen("notepad.exe")

    #time.sleep(2)

    #page = NotepadPage()
    #page.open_file_menu()