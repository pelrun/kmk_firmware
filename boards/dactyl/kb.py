import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic

class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.GP11, board.GP12, board.GP13, board.GP14, board.GP15)
    col_pins = (board.GP6, board.GP7, board.GP8, board.GP9, board.GP10)
    diode_orientation = DiodeOrientation.COLUMNS # FROM columns, TO rows. Bad naming scheme!
    data_pin = board.GP0
    data_pin2 = board.GP1

    debug_enabled = True

    coord_mapping = []
    coord_mapping.extend(ic(0, x) for x in range(10))
    coord_mapping.extend(ic(1, x) for x in range(10))
    coord_mapping.extend(ic(2, x) for x in range(10))
    # Now things get a little bit confusing!
    coord_mapping.extend(ic(3, x) for x in [1,2, 7,8])
    coord_mapping.extend(ic(3, x) for x in [3,4,0, 9,5,6])
    coord_mapping.extend(ic(4, x) for x in [4,0, 9,5])
