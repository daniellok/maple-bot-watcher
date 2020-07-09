#########################################################
#                                                       #
#                    BGRA Constants                     #
#                                                       #
#  The way entity detection works in this script is     #
#  by finding unique pixel colors. For example, in the  #
#  Maple minimap, strangers are indicated in pure red.  #
#  Therefore, to detect the presence of a stranger, we  #
#  simply need to check if the minimap contains any     #
#  red pixels.                                          #
#                                                       #
#  For more complicated situations, or situations in    #
#  which a unique color cannot be found, we can alter-  #
#  natively use a group of pixels.                      #
#                                                       #
#  These pixel values are in BGRA format to conform     #
#  with the OpenCV convention.                          #
#                                                       #
#########################################################

# Entity colors on the minimap
MINIMAP_ENTITY_BGRA = {
    'stranger' : [0,   0, 255, 255],
    'party'    : [0, 119, 255, 255],
}

# Entity colors for mobs in the main view
FRAME_ENTITY_BGRA = {
    'black_crow' : [0, 51, 255, 255],
}

# A group of pixels that uniquely identifies the death dialog
DEATH_DIALOG_BGRA = [
    [[221, 187, 170, 255],
     [238, 221, 204, 255],
     [238, 221, 204, 255]],
    [[170, 119,  85, 255],
     [255, 255, 255, 255],
     [255, 255, 255, 255]],
    [[170, 119,  85, 255],
     [255, 255, 255, 255],
     [255, 255, 255, 255]],
    [[153, 102,  51, 255],
     [238, 238, 238, 255],
     [238, 238, 238, 255]]
]


#########################################################
#                                                       #
#            Various screenshot coordinates             #
#                                                       #
#  The coordinates in this section correspond to the    #
#  locations of various things on the MSS screenshot.   #
#  The origin is the top-left, and the coords are in    #
#  the following form:                                  #
#                                                       #
#  (top_left_y, top_left_x, bot_right_y, bot_right_x)   #
#                                                       #
#########################################################

DEATH_DIALOG_COORDS = (409, 743, 413, 746)
MAP_MINIMAP_COORDS = {
    'tot'   : (140, 15, 390, 325),
    'himes' : (140, 15, 260, 415),
}
MAP_FRAME_COORDS = {
    'tot'   : (410, 0, 850, 1600),
    'himes' : (310, 0, 850, 1600),
}


#########################################################
#                                                       #
#              Maplestory Client Constants              #
#                                                       #
#  This section contains stuff that relates to your     #
#  MapleStory client.                                   #
#                                                       #
#########################################################

# Screen coords in the form (top_left_x, top_left_y, width, height).
# These coords are provided to MSS to define the screenshot area
MAPLE_CLIENT_SCREEN_COORDS = (0, 0, 800, 622)

# App name (e.g. the name it shows in your dock)
MAPLE_CLIENT_APP_NAME = ''


#########################################################
#                                                       #
#                Telegram API Constants                 #
#                                                       #
#  This section contains stuff for calling the Tele-    #
#  gram API.                                            #
#                                                       #
#########################################################

# The chat ID that you want to send your messages to
CHAT_ID = ''

# Your Telegram bot's API token
API_TOKEN = ''

# You shouldn't need to edit this
API_URL = 'https://api.telegram.org/bot{}/sendMessage'.format(API_TOKEN)

