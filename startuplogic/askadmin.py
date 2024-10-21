import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def ask_for_admin():
    if not is_admin():
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
        except:
            pass  # If the user denies elevation, do nothing here

def setup():
    ask_for_admin()
    if not is_admin():
        return  # Non-admin instance should continue without exiting
