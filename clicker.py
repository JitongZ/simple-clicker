import pyautogui
import time
import random
import argparse
import json
import ctypes
import os
import sys
from pynput import mouse

config_file = 'config.txt'

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if sys.version_info[0] == 3 and sys.version_info[1] >= 5:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    else:
        raise RuntimeError("This script requires Python 3.5 or higher")

def record_position():
    def on_click(x, y, button, pressed):
        if pressed and button == mouse.Button.left:
            position = {'x': x, 'y': y}
            with open(config_file, 'w') as file:
                json.dump(position, file)
            print(f"Position recorded: {position}")
            return False  # Stop listener

    print("Move the mouse to the desired position and click the left button.")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # Left button down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # Left button up

def run_clicker(repeat, delays, random_range):
    try:
        with open(config_file, 'r') as file:
            position = json.load(file)
    except FileNotFoundError:
        print(f"Error: The config file '{config_file}' does not exist. Please run the script with --position to record a position first.")
        return
    
    initial_position = pyautogui.position()

    def on_move(x, y):
        if (x, y) != initial_position:
            global running
            running = False
            print("Mouse moved! Stopping the program.")
            return False  # Stop the listener

    listener = mouse.Listener(on_move=on_move)
    listener.start()
    
    count = 0
    delay_index = 0
    global running
    running = True
    while running:
        click(position['x'], position['y'])
        count += 1
        if repeat != 'inf' and count >= int(repeat):
            break
        current_delay = delays[delay_index]
        delay_index = (delay_index + 1) % len(delays)
        sleep_time = current_delay + random.uniform(-random_range, random_range)
        time.sleep(sleep_time)
    
    listener.stop()
    print("Clicking task completed.")

def parse_delays(delay_str):
    try:
        return [float(d) for d in delay_str.strip("[]").split(",")]
    except ValueError:
        raise argparse.ArgumentTypeError("Delays must be a list of floats in the format '[delay1, delay2]'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto clicker with position recording and configurable delay.")
    parser.add_argument('--position', action='store_true', help="Record mouse position")
    parser.add_argument('--repeat', type=str, default='inf', help="Number of repetitions, 'inf' for infinite")
    parser.add_argument('--delay', type=parse_delays, default="[3.9]", help="Delay between clicks in seconds, in the format '[delay1, delay2]'")
    parser.add_argument('--random', type=float, default=0.1, help="Random range to add to the delay")

    args = parser.parse_args()

    if not is_admin():
        print("The script is not running with administrator privileges. Re-running with elevated permissions...")
        run_as_admin()
    else:
        if args.position:
            record_position()
        else:
            run_clicker(args.repeat, args.delay, args.random)
