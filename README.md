# simple-clicker
An auto clicker script that allows you to record a mouse position and perform automated clicks with configurable delays and randomization. This script is particularly useful for tasks that require repetitive clicking at a specific location on the screen.

## Features

- **Record Mouse Position:** Easily record the mouse position where you want the clicks to occur.
- **Configurable Click Delays:** Set delays between clicks, including alternating delays.
- **Randomization:** Add a random range to the delay to simulate more human-like behavior.
- **Stop on Mouse Move:** Automatically stop the clicking if the mouse is moved to prevent unwanted clicks.

## Prerequisites

- Python 3.5 or higher
- `pyautogui` library
- `pynput` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JitongZ/auto-clicker.git
   cd auto-clicker
   ```

2. Install the required libraries:
   ```bash
   pip install pyautogui pynput
   ```

## Usage

### Record Mouse Position

To record the mouse position, run the script with the `--position` argument. Move the mouse to the desired position and click the left mouse button to record the position.

```bash
python clicker.py --position
```

### Run the Auto Clicker

To run the auto clicker, use the desired configuration for repetitions, delay, and randomization.

- `--repeat`: Number of repetitions. Use `inf` for infinite repetitions.
- `--delay`: Delays between clicks in seconds, in the format `[delay1,delay2]` for alternating delays.
- `--random`: Random range to add to the delay.

```bash
python clicker.py --repeat inf --delay "[3.9]" --random 0.1
```

The above line uses the default values. You can also run without the arguments.
```bash
python clicker.py
```

Then, the program will prompt you to give permission to this app. Click "yes" or use your keyboard to navigate to "yes" and enter. Remember not to move your mouse because that will stop the program.


## Disclaimer

Use this tool responsibly. The author is not responsible for any misuse or damage caused by this tool.
