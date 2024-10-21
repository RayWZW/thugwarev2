import discord
import webbrowser

async def search(ctx, *, query: str):
    search_url = f"https://www.bing.com/search?q={query}"
    webbrowser.open(search_url)
    
    embed = discord.Embed(
        title="Searching on Bing",
        description=f"[Click here to see results]({search_url})",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)
