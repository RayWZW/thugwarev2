import win32gui
import win32api
import win32con
import ctypes
import math
import random
import threading
import time

is_running = False

error_icons = [
    win32con.IDI_ERROR,
    win32con.IDI_ASTERISK,
    win32con.IDI_HAND,
    win32con.IDI_QUESTION,
    win32con.IDI_INFORMATION,
    win32con.IDI_WARNING,
    win32con.IDI_WINLOGO,
]

def run_single_ring(bounce_height, center_x, center_y, num_icons_per_ring, move_speed):
    angle_offset = 0
    while is_running:
        hdc = win32gui.GetDC(0)
        bounce_offset = int(bounce_height * math.sin(time.time() * 10))
        
        radius = 30 + (1000 - 30) * (math.sin(time.time() * 2) + 1) / 2

        for i in range(num_icons_per_ring):
            angle = math.radians(i * (360 / num_icons_per_ring) + angle_offset)
            x = int(center_x + (radius + bounce_offset) * math.cos(angle))
            y = int(center_y + (radius + bounce_offset) * math.sin(angle))

            icon_type = random.choice(error_icons)
            win32gui.DrawIcon(hdc, x, y, win32gui.LoadIcon(None, icon_type))

        win32gui.ReleaseDC(0, hdc)
        angle_offset += move_speed * 2
        time.sleep(0.01)

def run_errorspamz_effect():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

    center_x, center_y = sw // 2, sh // 2
    num_rings = 10
    icons_per_ring = 30
    bounce_height = 50
    move_speed = 5

    threads = []

    for ring in range(num_rings):
        thread = threading.Thread(target=run_single_ring, args=(bounce_height, center_x, center_y, icons_per_ring, move_speed))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

async def errorspamz(ctx, action=None):
    global is_running

    if action == "start":
        if is_running:
            await ctx.send("Error spam effect is already running!")
            return
        is_running = True
        threading.Thread(target=run_errorspamz_effect).start()
        await ctx.send("Error spam effect started! Type `!errorspamz stop` to stop it.")

    elif action == "stop":
        if not is_running:
            await ctx.send("Error spam effect is not running!")
            return
        is_running = False
        await ctx.send("Error spam effect stopped.")

    else:
        await ctx.send(
            "Invalid action. Use `!errorspamz start` to start the error spam effect.\n"
            "Use `!errorspamz stop` to stop the error spam effect."
        )
