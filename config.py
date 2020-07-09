from utils import *

# The number of minutes you want to run for before quitting.
RUNTIME_MINS = 180

# The number of screenshots to take per second. More frequent
# screenshots allow you to quit faster when a player enters the map.
SCREENSHOTS_PER_SEC = 2

# Add the checks you want to perform here. The key names are the
# map names, and the values are a list of JSON-esque objects.
#
# The objects must contain the following keys:
#   'fn'    - The check to perform. The main script will run this function
#             and pass `img` in as an argument. `img` will be the full
#             screenshot returned by MSS. If the function returns True,
#             the main script will quit the MapleStory client.
#
#   'error' - The error message to display if the function returns True.
#             This error will be sent to you on Telegram, and also printed
#             out in the console.
MAP_CHECKS = {
    'tot' : [
        {
            'fn'    : lambda img: entity_in_minimap(img, 'stranger', 'tot'),
            'error' : 'A stranger entered the map.',
        },
        {
            'fn'    : lambda img: not entity_in_minimap(img, 'party', 'tot'),
            'error' : 'Your mage is no longer present.',
        },
        {
            'fn'    : lambda img: death_dialog_visible(img),
            'error' : 'You died.',
        },
    ],
    'himes' : [
        {
            'fn'    : lambda img: entity_in_minimap(img, 'stranger', 'himes'),
            'error' : 'A stranger entered the map.',
        },
        {
            'fn'    : lambda img: entity_in_frame(img, 'black_crow', 'himes'),
            'error' : 'Black Crow spawned.',
        },
        {
            'fn'    : lambda img: death_dialog_visible(img),
            'error' : 'You died.',
        },
    ],
}
