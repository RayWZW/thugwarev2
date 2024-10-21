import discord

async def clean(ctx):
    current_channel = ctx.channel
    guild = ctx.guild
    for channel in guild.channels:
        if channel != current_channel:
            await channel.delete()
    await ctx.send('All channels except the current one have been deleted.')
