"""
  Um bloco de notas minimalista criado com a estrutura PySimpleGUI 
"""
import PySimpleGUI as sg

sg.ChangeLookAndFeel("BrownBlue")  # Mudança do Tema

WIN_W: int = 90
WIN_H: int = 25
filename: str = None

# Variáveis ​​de string para reduzir o loop e o código do menu!
file_new: str = "New............(CTRL+N)"
file_open: str = "Open..........(CTRL+O)"
file_save: str = "Save............(CTRL+S)"

menu_layout: list = [
    ["File", [file_new, file_open, file_save, "Save As", "---", "Exit"]],
    ["Tools", ["Word Count"]],
    ["Help", ["About"]],
]

layout: list = [
    [sg.Menu(menu_layout)],
    [sg.Text("> New file <", font=("Consolas", 10), size=(WIN_W, 1), key="_INFO_")],
    [sg.Multiline(font=("Consolas", 12), size=(WIN_W, WIN_H), key="_BODY_")],
]

window: object = sg.Window(
    "Notepad",
    layout=layout,
    margins=(0, 0),
    resizable=True,
    return_keyboard_events=True,
)
window.read(timeout=1)
window.maximize()
window["_BODY_"].expand(expand_x=True, expand_y=True)


def new_file() -> str:
    """ Redefinir corpo e barra de informações e limpar variável de nome de arquivo! """
    window["_BODY_"].update(value="")
    window["_INFO_"].update(value="> New File <")
    filename = None
    return filename


def open_file() -> str:
    """ Abra o arquivo e atualize o infobar """
    try:
        filename: str = sg.popup_get_file("Open File", no_window=True)
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "r") as f:
            window["_BODY_"].update(value=f.read())
        window["_INFO_"].update(value=filename)
    return filename


def save_file(filename: str):
    """ Salve o arquivo instantaneamente se já estiver aberto; caso contrário, use o pop-up `save-as` """
    if filename not in (None, ""):
        with open(filename, "w") as f:
            f.write(values.get("_BODY_"))
        window["_INFO_"].update(value=filename)
    else:
        save_file_as()


def save_file_as() -> str:
    """ Salvar novo arquivo ou salvar o arquivo existente com outro nome """
    try:
        filename: str = sg.popup_get_file("Save File", save_as=True, no_window=True)
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "w") as f:
            f.write(values.get("_BODY_"))
        window["_INFO_"].update(value=filename)
    return filename


def word_count():
    """ Exibir contagem estimada de palavras """
    words: list = [w for w in values["_BODY_"].split(" ") if w != "\n"]
    word_count: int = len(words)
    sg.PopupQuick("Word Count: {:,d}".format(word_count), auto_close=False)


def about_me():
    sg.PopupQuick(
        '"Todas as grandes coisas têm pequenos começos "- Peter Senge', auto_close=False
    )


while True:
    event, values = window.read()

    if event in (None, "Exit"):
        break
    if event in (file_new, "n:78"):
        filename = new_file()
    if event in (file_open, "o:79"):
        filename = open_file()
    if event in (file_save, "s:83"):
        save_file(filename)
    if event in ("Save As",):
        filename = save_file_as()
    if event in ("Word Count",):
        word_count()
    if event in ("About",):
        about_me()

Notepad = Notepad()
Notepad.Iniciar()
