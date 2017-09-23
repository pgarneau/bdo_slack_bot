from ctypes import *
import win32service
import win32serviceutil
import win32api
import win32event
import win32evtlogutil
import os
import kb_input

from win32con import *
import time
import autoit


EnumWindows = windll.user32.EnumWindows
EnumWindowsProc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
GetWindowText = windll.user32.GetWindowTextW
GetWindowTextLength = windll.user32.GetWindowTextLengthW
IsWindowVisible = windll.user32.IsWindowVisible
GetClassName = windll.user32.GetClassNameW
BringWindowToTop = windll.user32.BringWindowToTop

titles = []

def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        classname = create_unicode_buffer(100 + 1)
        GetClassName(hwnd, classname, 100 + 1)
        buff = create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        titles.append((hwnd, buff.value, classname.value))
    return True

EnumWindows(EnumWindowsProc(foreach_window), 0)

def refresh_wins():
    del titles[:]
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    return titles

def get_hwnd_by_title_classname(wins, title, classname):
    for item in wins:
        if title in item[1] and classname in item[2]:
            return item[0], item[1]

def bring_bdo_top(wins):
    hwnd, title = get_hwnd_by_title_classname(wins, "BLACK DESERT",
                                       "BlackDesertWindowClass")
    if hwnd:
        bring_to_top(hwnd)

    return title

def bring_to_top(hWnd):
    windll.user32.ShowWindow(hWnd, 5);
    windll.user32.BringWindowToTop(hWnd);
    windll.user32.SetForegroundWindow(hWnd)

    return hWnd

def run():
    window = bring_bdo_top(refresh_wins())
    print(window)
    some_var = autoit.win_active(window)
    print(some_var)
    some_var_2 = autoit.win_activate(window)
    print(some_var_2)
    some_var = autoit.win_active(window)
    print(some_var)
    some_var = autoit.win_get_handle(window)
    time.sleep(2)
    autoit.control_send(window, "", "r")

if __name__=='__main__':
    run()
