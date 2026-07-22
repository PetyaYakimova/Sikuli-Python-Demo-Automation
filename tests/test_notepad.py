from pages.notepad_page import NotepadPage


def test_open_file_menu():
    page = NotepadPage()

    input("Open Notepad and press Enter...")

    page.open_file_menu()