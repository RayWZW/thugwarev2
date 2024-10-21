import os
import sys
import ctypes
from discord.ext import commands

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

async def admin_command(ctx):
    if is_admin():
        await ctx.send("The script is already running as Administrator.")
    else:
        await ctx.send("Attempting to elevate privileges...")
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, ' '.join(sys.argv), None, 1
            )
            sys.exit()
        except Exception as e:
            await ctx.send(f"Failed to elevate privileges: {str(e)}")
