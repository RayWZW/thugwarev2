import discord
import psutil
import os

async def lp(ctx):
    try:
        process_list = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
            try:
                process_info = f"PID: {proc.pid}\nName: {proc.name()}\nUsername: {proc.username()}\nCPU Percent: {proc.cpu_percent()}%\nMemory Percent: {proc.memory_percent()}\n"
                process_list.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        
        if not process_list:
            await ctx.send("No processes found or unable to access process details.")
            return
        
        file_content = "\n\n".join(process_list)
        with open('processes.txt', 'w', encoding='utf-8') as f:
            f.write(file_content)
        
        file = discord.File('processes.txt', filename='processes.txt')
        await ctx.send(file=file)
        
    except Exception as e:
        await ctx.send(f"An error occurred while fetching process details: {str(e)}")

    finally:
        if os.path.exists('processes.txt'):
            os.remove('processes.txt')
