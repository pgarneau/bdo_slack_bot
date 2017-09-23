from ctypes import *
import autoit

# windll Object Definitions
EnumWindows = windll.user32.EnumWindows
EnumWindowsProc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
GetWindowText = windll.user32.GetWindowTextW
GetWindowTextLength = windll.user32.GetWindowTextLengthW
IsWindowVisible = windll.user32.IsWindowVisible
GetClassName = windll.user32.GetClassNameW
BringWindowToTop = windll.user32.BringWindowToTop

BDO_CLASS = "BlackDesertWindowClass"
BDO_BASIC_TITLE = "BLACK DESERT"
TITLES = []

def _get_window_information(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        classname = create_unicode_buffer(100 + 1)
        GetClassName(hwnd, classname, 100 + 1)
        buff = create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        TITLES.append((hwnd, buff.value, classname.value))
    return True

def _get_all_windows():
    del TITLES[:]
    EnumWindows(EnumWindowsProc(_get_window_information), 0)
    return TITLES

def _focus_window(hwnd):
    windll.user32.ShowWindow(hwnd, 5);
    windll.user32.BringWindowToTop(hwnd);
    windll.user32.SetForegroundWindow(hwnd)

    return hwnd

def _get_bdo():
    windows = _get_all_windows()
    for window in windows:
        if BDO_BASIC_TITLE in window[1] and BDO_CLASS in window[2]:
            return window[0], window[1]

def focus_bdo():
    hwnd, title = _get_bdo()
    _focus_window(hwnd)
    autoit.win_activate(title)
    autoit.mouse_move(962, 526, speed=20)

    return title
