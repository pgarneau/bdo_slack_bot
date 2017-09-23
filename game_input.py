import time

import autoit

import window

COORDINATES = {
    "worker_button": [709, 546],
    "recover_button": [1496, 656],
    "confirm_recover_button": [1275, 335],
    "repeat_all_button": [1578, 653],
    "close_menu_button": [1242, 230]
}

menu_open = False

def open_menu():
    title = window.focus_bdo()
    autoit.control_send(title, "", "{ESC}")

def close_menu():
    title = window.focus_bdo()
    for _ in xrange(6):
        autoit.control_send(title, "", "{ESC}")
        time.sleep(1)

    left_click(COORDINATES.get("close_menu_button"))

def left_click(coords):
    title = window.focus_bdo()
    autoit.mouse_click(button="left", x=coords[0], y=coords[1], clicks=2,
                       speed=20)

def get_pos():
    x, y = autoit.mouse_get_pos()
    print(x)
    print(y)
