import discord
import threading
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class VolumeController:
    def __init__(self):
        self.running = False
        self.thread = None

    def set_volume_to_max(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        while self.running:
            volume.SetMasterVolumeLevelScalar(1.0, None)
            time.sleep(0.001)

    async def start_boost(self, ctx):
        if not self.running:
            self.running = True
            await ctx.send("Volume boost activated. System volume set to maximum.")
            self.thread = threading.Thread(target=self.set_volume_1000_times_per_second, daemon=True)
            self.thread.start()
        else:
            await ctx.send("Volume boost is already active.")

    def set_volume_1000_times_per_second(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        while self.running:
            volume.SetMasterVolumeLevelScalar(1.0, None)
            time.sleep(0.001)

    async def stop_boost(self, ctx):
        if self.running:
            self.running = False
            await ctx.send("Volume boost deactivated.")
        else:
            await ctx.send("Volume boost is not active.")

volume_controller = VolumeController()

async def bassboost(ctx, action: str):
    if action == "start":
        await volume_controller.start_boost(ctx)
    elif action == "stop":
        await volume_controller.stop_boost(ctx)
    else:
        await ctx.send("Invalid action. Use 'start' or 'stop'.")
