import time
import argparse
import config as cfg

from utils import *

# Set-up & Initialization
parser = argparse.ArgumentParser(
    description="This is a program to watch a MapleStory client " +
    "for visual events, and quit the client when they happen"
)
parser.add_argument('map_name', type=str, help="the name of the map")

args = parser.parse_args()
map_name = args.map_name

if map_name not in cfg.MAP_CHECKS:
    print('Unrecognized map name. Please choose from:')
    print(', '.join(cfg.MAP_CHECKS.keys()))
    print('\nAlternatively, add a new entry to config.map_constants')

    
# Main loop
checks = cfg.MAP_CHECKS[map_name]
start = time.time()

print('Watching...')
iterations = cfg.RUNTIME_MINS * 60 * cfg.SCREENSHOTS_PER_SEC
for i in range(iterations):
    time.sleep(1.0 / cfg.SCREENSHOTS_PER_SEC)
    img = take_screenshot()
    for obj in checks:
        check_result = obj['fn'](img)
        if check_result:
            end = time.time()
            msg = obj['error'] + ' Runtime: {:0.2f} seconds.'.format(end - start)
            print(msg)
            quit_apps()
            send_telegram_message(msg)
            exit(1)

print('Ending normally');
send_telegram_message("Time's up! Quitting the apps.")
quit_apps()
    
