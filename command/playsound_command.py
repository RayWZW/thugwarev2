import os
import threading
import time
import discord
import pygame
import random
import string

ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg'}
playing_sounds = {}

def generate_random_tag(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def play_sound(file_path, sound_key):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    playing_sounds[sound_key] = file_path
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    time.sleep(2)

async def playsound(ctx, action=None):
    if action == "stop":
        sound_key = ctx.guild.id
        if sound_key in playing_sounds:
            pygame.mixer.music.stop()
            playing_sounds.pop(sound_key, None)
            await ctx.send("Stopped playback.")
        else:
            await ctx.send("No sound is currently playing.")
    elif ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        temp_dir = os.path.join(os.path.dirname(__file__), 'temp_sounds')
        os.makedirs(temp_dir, exist_ok=True)
        original_name, ext = os.path.splitext(attachment.filename)
        random_tag = generate_random_tag()
        sound_file_path = os.path.join(temp_dir, f"{original_name}_{random_tag}{ext}")

        if attachment.filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS:
            await attachment.save(sound_file_path)
            sound_key = ctx.guild.id
            time.sleep(2)
            threading.Thread(target=play_sound, args=(sound_file_path, sound_key)).start()
            await ctx.send(f"Playing sound: {attachment.filename}")
