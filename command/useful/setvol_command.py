import discord
from discord.ext import commands
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

async def vol_command(ctx, volume: int):
    if 1 <= volume <= 100:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_control = cast(interface, POINTER(IAudioEndpointVolume))

        volume_level = volume / 100.0
        volume_control.SetMasterVolumeLevelScalar(volume_level, None)

        await ctx.send(f"Volume set to **{volume}**%.")
    else:
        await ctx.send("Please provide a volume level between **1** and **100**.")
