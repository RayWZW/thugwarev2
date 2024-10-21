import discord
import psutil

async def kp(ctx, name_or_pid: str):
    try:
        pid = int(name_or_pid)
        proc = psutil.Process(pid)
        proc.terminate()
        await ctx.send(f"Process {proc.pid} ({proc.name()}) terminated.")
    except ValueError:
        found = False
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if name_or_pid.lower() in proc.info['name'].lower() or (proc.info['cmdline'] and name_or_pid.lower() in ' '.join(proc.info['cmdline']).lower()):
                proc_obj = psutil.Process(proc.info['pid'])
                proc_obj.terminate()
                await ctx.send(f"Process {proc_obj.pid} ({proc_obj.name()}) terminated.")
                found = True
        if not found:
            await ctx.send("Process not found.")
    except psutil.NoSuchProcess:
        await ctx.send("Process not found.")
