import os
import cv2
import numpy as np
import time
import random

ip = '127.0.0.1'
port = '5745'
emulator = str(f'{ip}:{port}')

# Executes a given command in the system shell and suppresses output
def run_cmd(command):
    os.system(command + ' > NUL')

# Simulates a touchscreen tap at the specified (x, y) coordinates
def click_position(x, y):
    run_cmd(f'adb shell input touchscreen tap {x} {y}')

# Captures a screenshot from the device and moves it to the images directory
def screenshot_pull():
    run_cmd(f'adb shell screencap -p /sdcard/screenshot.png')
    run_cmd(f'adb pull /sdcard/screenshot.png')



# Waits for a specific image to appear on screen, then clicks to exit it
def recognize_image(image_path, threshold, x, y):
    while True:
        screenshot_pull()  # Take a new screenshot
        time.sleep(0.5)  # Pause before checking again
        
        img, tpl = cv2.imread('screenshot.png', 0), cv2.imread(image_path, 0)
        result = cv2.matchTemplate(img, tpl, cv2.TM_CCOEFF_NORMED)
        locs = cv2.findNonZero((result > threshold).astype(np.uint8))
        
        if locs is not None:
            click_position(x, y)  # Click to exit menu
            os.remove('screenshot.png')
            break

def generate_coordinates(a, b): # Lowest to Highest
    n = random.sample(range(a, b), 1)[0]
    return str(n)

def rokbot():
    os.system('adb disconnect')
    os.system(f'adb connect {emulator}')

    os.system('cls')
    
    recognize_image(image_path='images/tutorial_lady/1.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 1')
    time.sleep(0.3)

    recognize_image(image_path='images/tutorial_lady/2.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 2')
    time.sleep(0.3)

    recognize_image(image_path='images/tutorial_lady/3.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 3')
    time.sleep(2)

    recognize_image(image_path='images/tutorial_lady/4.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 4')
    time.sleep(2)

    recognize_image(image_path='images/tutorial_lady/5.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 5')
    time.sleep(2)

    click_position(x=generate_coordinates(40, 100), y=generate_coordinates(650, 700)) # Build Menu ,,, Reuse for barb search
    print('Build Menu')
    time.sleep(2)

    click_position(x=332, y=539) # Place Farm
    print('Place Farm')
    time.sleep(1)

    recognize_image(image_path='images/exit.png', threshold=0.3, x=925, y=450) # Confirm Farm Placement
    print('Confirm Farm Placement')
    time.sleep(4)

    click_position(x=generate_coordinates(794, 839), y=generate_coordinates(550, 590)) # Collect Food
    print('Collect Food')
    time.sleep(0.3)

    recognize_image(image_path='images/tutorial_lady/6.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 6')
    time.sleep(4)

    recognize_image(image_path='images/villager/1.png', threshold=0.2, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Villager Dialogue - 1')
    time.sleep(1.5)

    recognize_image(image_path='images/villager/2.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Villager Dialogue - 2')
    time.sleep(2)

    recognize_image(image_path='images/system/1.png', threshold=0.3, x=79, y=821) # System Quest
    print('Completed System Quest')
    time.sleep(1)

    recognize_image(image_path='images/tutorial_lady/7.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 7')
    time.sleep(1)

    recognize_image(image_path='images/barbarian/1.png', threshold=0.3, x=30, y=800) # System Quest
    print('Completed Barbarian Dialogue - 1')
    time.sleep(1)

    recognize_image(image_path='images/system/2.png', threshold=0.3, x=30, y=800) # System Quest
    print('Completed System Quest')

    recognize_image(image_path='images/tutorial_lady/8.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 8')
    time.sleep(1)

    click_position(x=generate_coordinates(578, 722), y=generate_coordinates(492, 611))
    print('Clicked Barracks')
    time.sleep(0.4)

    click_position(x=generate_coordinates(770, 870), y=generate_coordinates(680, 750))
    print('Clicked Training Icon')
    time.sleep(0.5)

    click_position(x=generate_coordinates(1120, 1320), y=generate_coordinates(710, 760))
    print('Training Troops')
    time.sleep(5)
    
    click_position(x=generate_coordinates(578, 722), y=generate_coordinates(492, 611))
    print('Collecting Troops')
    time.sleep(0.5)

    recognize_image(image_path='images/tutorial_lady/9.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 9')
    time.sleep(1.3)
    
    click_position(x=814, y=416)
    print('Clicked Wall')
    time.sleep(0.7)

    click_position(x=805, y=586)
    print('Upgrade Menu')
    time.sleep(1)

    click_position(x=1223, y=682)
    print('Upgrading Wall')
    time.sleep(3)

    recognize_image(image_path='images/tutorial_lady/10.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 10')
    time.sleep(0.5)
    
    recognize_image(image_path='images/tutorial_lady/11.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Tutorial Lady Dialogue - 11')
    time.sleep(1)

    click_position(x=generate_coordinates(40, 100), y=generate_coordinates(650, 700)) # Build Menu
    print('Build Menu')
    time.sleep(2)

    click_position(x=74, y=638) # Military Buildings Menu
    print('Build Menu')
    time.sleep(2)

    click_position(x=332, y=539) # Place Tavern
    print('Place Farm')
    time.sleep(1)

    click_position(x=431, y=272) # Confirm Tavern Placement
    print('Confirm Tavern Placement')
    time.sleep(4)

    click_position(x=506, y=629) # Tavern Menu
    print('Tavern Menu')
    time.sleep(1)

    click_position(x=1093, y=756) # Open Gold Key
    print('Opening Gold Key')
    time.sleep(5)

    click_position(x=253, y=756) # Commander Confirm
    print('Confirm Commander Recruit')
    time.sleep(1)

    click_position(x=577, y=799) # Tavern Confirm
    print('Confirm Tavern')
    time.sleep(1)

    click_position(x=40, y=40) # Exit Tavern
    print('Exiting Tavern')
    time.sleep(1.6)

    click_position(x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    time.sleep(0.7)

    click_position(x=79, y=821) # System Quest
    print('Go to map')
    time.sleep(1)

    click_position(x=generate_coordinates(40, 100), y=generate_coordinates(650, 700)) # Search Menu
    print('Search Menu')
    time.sleep(2)

    click_position(x=285, y=617) # Search Barbs
    print('Search for Barbs')
    time.sleep(1)

    click_position(x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900)) # Barb dialogue
    time.sleep(1.3)

    click_position(x=800, y=450)
    time.sleep(0.1)
    click_position(x=800, y=450)
    print('Select barbarian')
    time.sleep(1.5)

    click_position(x=1059, y=597)
    print('Attack barbarian')
    time.sleep(1)

    click_position(x=1204, y=188)
    print('New troop')
    time.sleep(1)

    click_position(x=480, y=453)
    print('Select commander')
    time.sleep(1)

    click_position(x=101, y=250)
    print('Select starting commander')
    time.sleep(1)

    click_position(x=1157, y=796)
    print('March')
    time.sleep(1)

    recognize_image(image_path='images/markswoman.png', threshold=0.3, x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900))
    print('Completed Markswoman Dialogue - 1')
    time.sleep(2)

    click_position(x=generate_coordinates(1, 1600), y=generate_coordinates(1, 900)) # Barb dialogue


rokbot()