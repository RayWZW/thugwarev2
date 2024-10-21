import discord
import webbrowser

async def openurl(ctx, *, url: str):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    webbrowser.open(url)
    
    embed = discord.Embed(
        title="Opening URL",
        description=f"[Click here to visit]({url})",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)
