import subprocess
from pydbus import SystemBus
from gi.repository import GLib
import os

# === CONFIG ===
base_dir = os.path.expanduser("~/.config/autostart/wallpaperFolder")
charging_wallpaper = os.path.join(base_dir, "charging.jpg")
discharging_wallpaper = os.path.join(base_dir, "battery.jpg")

# === WALLPAPER CHANGER ===
def set_wallpaper(path):
    try:
        subprocess.run([
            "gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{path}"
        ], check=True)
        subprocess.run([
            "gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", f"file://{path}"
        ], check=True)
        subprocess.run(["feh", "--bg-scale", path], check=True)
    except:
        pass

# === SIGNAL HANDLER ===
def handle_properties_changed(sender, object, iface, signal, params):
    try:
        changed = params[1]
        if 'Online' in changed:
            if changed['Online']:
                set_wallpaper(charging_wallpaper)
            else:
                set_wallpaper(discharging_wallpaper)
    except:
        pass

# === INITIAL STATE ===
def check_initial_state():
    try:
        output = subprocess.check_output([
            "upower", "-i", "/org/freedesktop/UPower/devices/line_power_ADP1"
        ]).decode()
        if "online: yes" in output:
            set_wallpaper(charging_wallpaper)
        else:
            set_wallpaper(discharging_wallpaper)
    except:
        pass

# === MAIN RUNNER ===
try:
    bus = SystemBus()
    loop = GLib.MainLoop()
    bus.subscribe(
        iface="org.freedesktop.DBus.Properties",
        object="/org/freedesktop/UPower/devices/line_power_ADP1",
        signal="PropertiesChanged",
        signal_fired=handle_properties_changed
    )
    check_initial_state()
    loop.run()

except:
    pass

