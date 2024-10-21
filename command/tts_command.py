import pyttsx3
import threading
from discord.ext import commands

engine = pyttsx3.init()
engine.setProperty('rate', 130)

def speak_in_background(message):
    engine.say(message)
    engine.runAndWait()

async def speak_command(ctx, *, message: str):
    await ctx.send(f"Saying: {message}")
    threading.Thread(target=speak_in_background, args=(message,)).start()
