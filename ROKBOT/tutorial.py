import os
import cv2
import numpy as np
import time
import random

port = '5945'
emulator = str(f'127.0.0.1:{port}')

# Executes a given command in the system shell and suppresses output
def run_cmd(command):
    os.system(command + ' > NUL')

# Simulates a touchscreen tap at the specified (x, y) coordinates
def click_position(x, y):
    run_cmd(f'adb -s {emulator} shell input touchscreen tap {x} {y}')

# Captures a screenshot from the device and moves it to the images directory
def screenshot_pull():
    run_cmd(f'adb -s {emulator} shell screencap -p /sdcard/screenshot.png')
    run_cmd(f'adb -s {emulator} pull /sdcard/screenshot.png')

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

def recognize_image_location(image_path, threshold):
    while True:
        screenshot_pull()  # Take a new screenshot
        time.sleep(0.5)  # Pause before checking again
        
        img, tpl = cv2.imread('screenshot.png', 0), cv2.imread(image_path, 0)
        result = cv2.matchTemplate(img, tpl, cv2.TM_CCOEFF_NORMED)
        locs = cv2.findNonZero((result > threshold).astype(np.uint8))
        
        if locs is not None:
            (x, y, w, h) = cv2.boundingRect(locs.astype(np.int32).squeeze())
            return (x, y)

def generate_coordinates(a, b): # Lowest to Highest
    n = random.sample(range(a, b), 1)[0]
    return str(n)

def recognize_and_click(image_path, threshold, x, y, message):
    recognize_image(image_path=image_path, threshold=threshold, x=x, y=y)
    print(message)
    time.sleep(1)

def click_and_log(x, y, message, sleep_time=1):
    click_position(x, y)
    print(message)
    time.sleep(sleep_time)

def tutorial():
    run_cmd('adb disconnect')
    run_cmd(f'adb connect {emulator}')
    run_cmd('cls')
    
    # Complete tutorial dialogues
    for i in range(1, 6):
        click_and_log(generate_coordinates(200, 1300), generate_coordinates(200, 600), f'Completed Tutorial Lady Dialogue - {i}', 2)
    
    click_and_log(75, 677, 'Build Menu', 2)
    click_and_log(332, 539, 'Place Farm', 1)
    click_and_log(925, 450, 'Confirm Farm Placement', 4)
    click_and_log(816, 568, 'Collect Food', 2)
    click_and_log(generate_coordinates(200, 1300), generate_coordinates(200, 600), 'Completed Tutorial Lady Dialogue - 6', 3)
    
    for i in range(1, 3):
        click_and_log(generate_coordinates(200, 1300), generate_coordinates(200, 600), f'Completed Villager Dialogue - {i}', 2)
    
    click_and_log(30, 821, 'Completed System Quest', 1)
    recognize_and_click('images/tutorial_lady/7.png', 0.3, generate_coordinates(200, 1300), generate_coordinates(200, 600), 'Completed Tutorial Lady Dialogue - 7')
    recognize_and_click('images/barbarian/1.png', 0.3, 30, 800, 'Completed Barbarian Dialogue - 1')
    click_and_log(30, 821, 'Completed System Quest', 2)
    click_and_log(generate_coordinates(200, 1300), generate_coordinates(200, 600), 'Completed Tutorial Lady Dialogue - 8', 1)
    click_and_log(generate_coordinates(578, 722), generate_coordinates(492, 611), 'Clicked Barracks', 0.4)
    click_and_log(generate_coordinates(770, 870), generate_coordinates(680, 750), 'Clicked Training Icon', 0.5)
    click_and_log(generate_coordinates(1120, 1320), generate_coordinates(710, 760), 'Training Troops', 5)
    click_and_log(generate_coordinates(578, 722), generate_coordinates(492, 611), 'Collecting Troops', 0.5)
    recognize_and_click('images/tutorial_lady/9.png', 0.3, generate_coordinates(200, 1300), generate_coordinates(200, 600), 'Completed Tutorial Lady Dialogue - 9')
    click_and_log(814, 416, 'Clicked Wall', 0.7)
    click_and_log(805, 586, 'Upgrade Menu', 1)
    click_and_log(1223, 682, 'Upgrading Wall', 3)
    recognize_and_click('images/tutorial_lady/10.png', 0.3, generate_coordinates(200, 1300), generate_coordinates(200, 600), 'Completed Tutorial Lady Dialogue - 10')
    recognize_and_click('images/tutorial_lady/11.png', 0.3, generate_coordinates(200, 1300), generate_coordinates(200, 600), 'Completed Tutorial Lady Dialogue - 11')
    
    # Tavern
    click_and_log(75, 677, 'Build Menu', 2)
    click_and_log(74, 638, 'Military Buildings Menu', 2)
    click_and_log(332, 539, 'Place Tavern', 1)
    click_and_log(431, 272, 'Confirm Tavern Placement', 4)
    click_and_log(506, 629, 'Tavern Menu', 1)
    click_and_log(1093, 756, 'Opening Gold Key', 5)
    click_and_log(253, 756, 'Confirm Commander Recruit', 1)
    click_and_log(577, 799, 'Confirm Tavern', 1)
    click_and_log(40, 40, 'Exiting Tavern', 1.6)
    click_and_log(generate_coordinates(200, 1300), generate_coordinates(200, 600), '', 0.7)
    click_and_log(79, 821, 'Go to map', 1)
    click_and_log(75, 677, 'Search Menu', 2)
    click_and_log(285, 617, 'Search for Barbs', 1)
    click_and_log(generate_coordinates(200, 1300), generate_coordinates(200, 600), '', 1.3)
    
    # Barbarians
    x, y = recognize_image_location('images/barb_select_tooltip.png', 0.3)
    click_and_log(x+300, y-100, 'Select Barbarian', 1)
    click_and_log(1059, 597, 'Attack barbarian', 1)
    click_and_log(1204, 188, 'New troop', 1)
    click_and_log(480, 453, 'Select commander', 1)
    click_and_log(101, 250, 'Select starting commander', 1)
    click_and_log(1157, 796, 'March', 1)
    recognize_and_click('images/markswoman.png', 0.3, generate_coordinates(200, 1300), generate_coordinates(200, 600), 'Completed Markswoman Dialogue - 1')
    click_and_log(generate_coordinates(200, 1300), generate_coordinates(200, 600), 'Barb dialogue')

def test_functs():
    None
    
tutorial()