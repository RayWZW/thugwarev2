import os
import ctypes
import requests

async def wallpaper(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        file_path = f"./{attachment.filename}"
        await attachment.save(file_path)
    else:
        file_path = "./default_wallpaper.jpg"
        response = requests.get("https://chochox.com/wp-content/uploads/2016/10/Gheto_29.jpg")
        with open(file_path, "wb") as f:
            f.write(response.content)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(file_path), 0)
    await ctx.send("Desktop wallpaper updated!")

    if os.path.exists(file_path):
        os.remove(file_path)
