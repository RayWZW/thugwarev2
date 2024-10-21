import discord
from discord.ext import commands
import ctypes
import threading
import sys

blocking = False
block_thread = None

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def block_input():
    ctypes.windll.user32.BlockInput(True)
    while blocking:
        pass

async def nomouse_command(ctx, action: str):
    global blocking, block_thread
    if not is_admin():
        await ctx.send("This command requires admin privileges. Please run the bot as an administrator.")
        return

    if action.lower() not in ['start', 'stop']:
        await ctx.send("Please use `start` or `stop`.")
        return

    if action.lower() == 'start':
        if blocking:
            await ctx.send("Mouse input is already blocked.")
            return
        
        blocking = True
        await ctx.send("Blocking mouse input...")
        block_thread = threading.Thread(target=block_input, daemon=True)
        block_thread.start()
        await ctx.send("Mouse input is now blocked.")
    
    elif action.lower() == 'stop':
        if not blocking:
            await ctx.send("Mouse input is not currently blocked.")
            return
        
        await ctx.send("Unblocking mouse input...")
        blocking = False
        ctypes.windll.user32.BlockInput(False)
        await ctx.send("Mouse input is now unblocked.")
