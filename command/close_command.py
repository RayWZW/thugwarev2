import os
import signal
from discord.ext import commands

async def close_command(ctx):
    await ctx.send("Shutting down...")
    os.kill(os.getpid(), signal.SIGTERM)
