import discord
import os

async def restartpc(ctx):
    os.system("shutdown /r /t 0")
    await ctx.send("The PC will restart now.")
