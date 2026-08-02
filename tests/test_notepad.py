from pages.notepad_page import NotepadPage


def test_open_file_menu(notepad):
    page = NotepadPage()

    page.open_file_menu()
