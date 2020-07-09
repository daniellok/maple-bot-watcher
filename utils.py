import os
import cv2
import mss
import requests
import numpy as np

from constants import *

def find_match(img, pixel_bgra):
    """ Returns True if the given image contains the given pixel.
    `coords` contains the coordinates of the matches, which you
    can inspect for debugging purposes.

    Args:
    img - the image to scan through
    pixel_bgra - the BGRA values of the pixel to find
    """
    indices = np.where(np.all(img == pixel_bgra, axis=-1))
    coords = list(zip(indices[1], indices[0]))
    return len(coords) > 0

def entity_in_minimap(img, entity, map_name):
    """Checks whether the given entity is in the minimap.

    Args:
    img - the full screenshot returned by MSS
    entity - the name of the entity
    map_name - the name of the map
    """
    if entity not in MINIMAP_ENTITY_BGRA:
        print(entity, 'not in constants.MINIMAP_ENTITY_BGRA')
    if map_name not in MAP_MINIMAP_COORDS:
        print(map_name, 'not in constants.MAP_MINIMAP_COORDS')

    row1, col1, row2, col2 = MAP_MINIMAP_COORDS[map_name]
    entity_bgra = MINIMAP_ENTITY_BGRA[entity]
    minimap = img[row1:row2, col1:col2]

    return find_match(minimap, entity_bgra)

def death_dialog_visible(img):
    """Checks if your character has died (i.e. if the death dialog
    is visible).

    Args:
    img - the full screenshot returned by MSS
    """
    row1, col1, row2, col2 = DEATH_DIALOG_COORDS
    death_dialog = img[row1:row2, col1:col2]
    
    return np.all(death_dialog == DEATH_DIALOG_BGRA)

def entity_in_frame(img, entity, map_name):
    """Checks if the given entity can be found in the main visual
    area of the game. Useful for detecting if bosses spawn.

    Args:
    img - the full screenshot returned by MSS
    entity - the name of the entity
    map_name - the name of the map
    """
    if entity not in FRAME_ENTITY_BGRA:
        print(entity, 'not in constants.FRAME_ENTITY_BGRA')
    if map_name not in MAP_FRAME_COORDS:
        print(map_name, 'not in constants.MAP_FRAME_COORDS')

    row1, col1, row2, col2 = MAP_FRAME_COORDS[map_name]
    entity_bgra = FRAME_ENTITY_BGRA[entity]
    frame = img[row1:row2, col1:col2]

    return find_match(frame, entity_bgra)

def take_screenshot():
    """Takes a screenshot and returns a numpy array that can be
    parsed by OpenCV functions. Note that the result is a 3D array
    of pixel values in BGRA format.

    On Retina screens, the image dimensions will be double that
    of the provided screen coords. For example, if you're taking a
    screenshot of the standard 800x600 client, your image size
    will actually be 1600x1200.
    """
    x1, y1, x2, y2 = MAPLE_CLIENT_SCREEN_COORDS
    monitor = {
        "top": x1,
        "left": y1,
        "width": x2,
        "height": y2,
    }
    with mss.mss() as sct:
        img = np.array(sct.grab(monitor))
    return img

def quit_apps():
    """Quits the MapleStory client and Automator. This works by
    making system calls to AppleScript, but you could probably
    modify this just to SIGKILL them. Supposedly this makes them
    quit gracefully, as though you pressed CMD + Q.
    """
    os.system("osascript -e 'tell app \"{}\" to quit saving no'".format(
        MAPLE_CLIENT_APP_NAME
    ))
    os.system("osascript -e 'tell app \"Automator\" to quit saving no'")

def send_telegram_message(message):
    """Sends the given message to a chat you specify in constants.CHAT_ID.
    
    Args:
    message - the message to send
    """
    params = {
        'chat_id': CHAT_ID,
        'text': message,
    }
    requests.post(API_URL, params)
