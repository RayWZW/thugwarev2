import discord
import os

async def shutdownpc(ctx):
    os.system("shutdown /s /t 0")
    await ctx.send("The PC will shut down now.")
