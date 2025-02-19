import os

def run_cmd(command):
    os.system(command + ' > NUL')

run_cmd(f'adb shell screencap -p /sdcard/screenshot.png')
run_cmd(f'adb pull /sdcard/screenshot.png')