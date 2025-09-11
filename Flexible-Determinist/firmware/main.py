# type: ignore[reportMissingImports]

print(" ------- Starting ---------")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes
from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord
from kmk.modules.holdtap import HoldTap


# SETUP THE MATRIX
keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.col_pins = (board.A2, board.A3, board.D11, board.D12, board.D9)
keyboard.row_pins = (board.D5, board.D6, board.D10, board.D13, board.A5, board.A4, board.A1, board.A0)

keyboard.coord_mapping = [
 0,  1,  2,  3,  4, 24, 23, 22, 21, 20,
 5,  6,  7,  8,  9, 29, 28, 27, 26, 25,
10, 11, 12, 13, 14, 34, 33, 32, 31, 30,
        17, 18, 19, 39, 38, 37
]

rgb = RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=1,
    val_default=0,
    animation_mode=AnimationModes.STATIC
)
keyboard.extensions.append(rgb)

_____ = KC.NO

# LAYERS
class RGBLayers(Layers):
    def activate_layer(self, keyboard, layer, idx=None):
        super().activate_layer(keyboard, layer, idx)
        if layer == 0:
            rgb.set_hsv_fill(0, 0, 0)
            rgb.show()
        else:
            rgb.set_hsv_fill(195, 255, 5)
            rgb.show()

keyboard.modules.append(RGBLayers())
TO_ZERO = KC.FD(0)
TO_ONE = KC.FD(1)

# MACROS
DELETE_WORD = KC.LALT(KC.BSPACE)

# CHORDS
combos = Combos()
combos.combos = [
    Chord((KC.LSHIFT, KC.SPACE), KC.TAB, timeout=100),
]
keyboard.modules.append(combos)

# HOLD
keyboard.modules.append(HoldTap())
HOLD_Z_SHIFT = KC.HT(KC.Z, KC.LSHIFT)
HOLD_SLASH_SHIFT = KC.HT(KC.SLASH, KC.RSHIFT)
HOLD_SPACE_GUI = KC.HT(KC.SPACE, KC.LGUI)
HOLD_ENTER_OPT = KC.HT(KC.ENTER, KC.LALT)
HOLD_BSPACE_DELWORD = KC.HT(KC.BSPACE, DELETE_WORD)

# KEYMAP
# [ ] arrows on bottom?
# [x] command on space hold
# [x] option on enter hold
# \ move tab to right 2
# \ hold p for backspace?
# [ ] no "home" or "end"


keyboard.keymap = [
#                                           LAYER 1
[
KC.Q,        KC.W,     KC.E,      KC.R,      KC.T,         KC.Y,       KC.U,       KC.I,       KC.O,   KC.P,
KC.A,        KC.S,     KC.D,      KC.F,      KC.G,         KC.H,       KC.J,       KC.K,       KC.L,   KC.QUOTE,
HOLD_Z_SHIFT, KC.X,     KC.C,      KC.V,      KC.B,         KC.N,       KC.M,       KC.COMMA,   KC.DOT, HOLD_SLASH_SHIFT,
                    TO_ONE,    KC.LCTRL,  HOLD_ENTER_OPT,    HOLD_SPACE_GUI,   HOLD_BSPACE_DELWORD,  _____
],


#                                           LAYER 2
[
KC.PGUP,   _____,  KC.UP,     _____,       KC.LCTL,    KC.EQL,   KC.N7,      KC.N8,    KC.N9,     _____,
KC.PGDOWN, KC.LEFT,  KC.DOWN,   KC.RIGHT,  KC.LALT,    _____,  KC.N4,      KC.N5,    KC.N6,  _____,
KC.LBRC,   KC.RBRC,  KC.BSLASH, KC.SCOLON, KC.TAB,     KC.N0,    KC.N1,      KC.N2,    KC.N3,  KC.ESC,    
                     TO_ZERO,   KC.LCTRL,   HOLD_ENTER_OPT,   HOLD_SPACE_GUI, HOLD_BSPACE_DELWORD,  KC.BT_NXT
]
]


if __name__ == '__main__':
    keyboard.go(
        hid_type=HIDModes.USB,
        secondary_hid_type=HIDModes.BLE,
        ble_name='Flexible Determinist'
    )
    # keyboard.go()
