🔌 Charging Wallpaper Changer

Automatically changes your desktop wallpaper based on your laptop’s charging state (charging or on battery).

🚀 Features

Detects charging vs discharging in real-time using D-Bus (UPower)

Automatically switches between two wallpapers

Works on GNOME-based Linux systems

One-time setup: runs automatically at login

🛠️ Setup Instructions

1. Clone the Repository

git clone https://github.com/Sujal7422/charging-wallpaper-changer.git
cd charging-wallpaper-changer

2. Place Wallpapers

Put your wallpapers in:

~/.config/autostart/wallpaperFolder/

Example file names:

charging.jpg

battery.jpg

3. Update Script and Desktop Entry (if needed)

If your username or paths differ, edit these:

wallpaper_changer.py

charging-wallpaper.desktop

4. Enable Auto-start

cp wallpaper_changer.py ~/.config/autostart/
cp charging-wallpaper.desktop ~/.config/autostart/

Ensure wallpapers are in:

~/.config/autostart/wallpaperFolder/

Make sure the script is executable:

chmod +x ~/.config/autostart/wallpaper_changer.py

You’re done! It will now run on every login.

⚙️ Path Customization

File

What to Change

Example

Notes

wallpaper_changer.py

charging_wallpaper and discharging_wallpaper paths

~/.config/autostart/wallpaperFolder/charging.jpg

Must point to actual image paths

wallpaper_changer.py

log_file path

~/.config/autostart/wallpaper_changer.log

Optional: can disable logging

wallpaper_changer.py

UPower device path

/org/freedesktop/UPower/devices/line_power_ADP1

Use upower -e to find yours

charging-wallpaper.desktop

Exec field

python3 /full/path/to/wallpaper_changer.py

Use full path or $HOME/...

🔍 How to Find Your UPower Path

Use this command:

upower -e

You’ll see something like:

/org/freedesktop/UPower/devices/line_power_ADP1

Update the script:

object="/org/freedesktop/UPower/devices/line_power_ADP1"

🧪 Troubleshooting

❌ Wallpaper doesn't change?

Check that the image paths are valid

Try running the script manually to test:

python3 ~/.config/autostart/wallpaper_changer.py

Ensure feh is installed:

sudo apt install feh

🟡 Log not rotating?

Make sure the log path is writable

Script will auto-rotate if it exceeds 1MB

💡 PropertiesChanged not firing?

Double-check the power device path with upower -e

📂 File Structure Example

~/.config/autostart/
├── wallpaperFolder/
│   ├── charging.jpg
│   └── battery.jpg
├── charging-wallpaper.desktop
└── wallpaper_changer.py

📜 License

MIT

👤 Author

Sujal Viradiya


