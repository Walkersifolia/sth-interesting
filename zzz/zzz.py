import win32api
import win32con
import time
import threading
import sys
import ctypes

def main():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def request_admin():
    if main():
        return
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

click_enabled = False

def click_mouse():
    x, y = win32api.GetCursorPos()

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.04)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def toggle_click():
    global click_enabled
    click_enabled = not click_enabled
    if click_enabled:
        print("ON")
    else:
        print("OFF")

def mouse_listener():
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_XBUTTON2) < 0:
            toggle_click()
            time.sleep(0.2)

if main():
    mouse_thread = threading.Thread(target=mouse_listener)
    mouse_thread.daemon = True
    mouse_thread.start()

    while True:
        if click_enabled:
          click_mouse()
          time.sleep(0.8)
          click_mouse()
          time.sleep(6.8)
else:
    print("请点击“是”以管理员模式运行此程序")
    request_admin()

if __name__ == "__main__":
    main()
