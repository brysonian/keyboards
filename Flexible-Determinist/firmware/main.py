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

# KEYMAP
keyboard.keymap = [
#                                           LAYER 1
[
KC.Q,   KC.W,  KC.E,    KC.R,       KC.T,                KC.Y,       KC.U,       KC.I,       KC.O,   KC.P,
KC.A,   KC.S,  KC.D,    KC.F,       KC.G,                KC.H,       KC.J,       KC.K,       KC.L,   KC.QUOTE,
KC.Z,   KC.X,  KC.C,    KC.V,       KC.B,                KC.N,       KC.M,       KC.COMMA,   KC.DOT, KC.SLASH,    
               TO_ONE,  KC.ENTER,   KC.RGB_TOG,          KC.SPACE,   KC.BSPACE,  DELETE_WORD
],


#                                           LAYER 2
[

KC.PGUP,   KC.HOME,  KC.UP,     KC.END,    KC.LCTL,      KC.EQL,   KC.N7,      KC.N8,    KC.N9,   KC.PSLS,
KC.PGDOWN, KC.LEFT,  KC.DOWN,   KC.RIGHT,  KC.LALT,      KC.PAST,  KC.N4,      KC.N5,    KC.N6,   KC.PMNS,
KC.LBRC,   KC.RBRC,  KC.BSLASH, KC.SCOLON, KC.TAB,       KC.N0,    KC.N1,      KC.N2,    KC.N3,   KC.PSLS,    
                     TO_ZERO,   KC.ENTER,  KC.LSHIFT,    KC.SPACE, KC.BSPACE,  KC.DEL
]
]


if __name__ == '__main__':
    keyboard.go()
    # keyboard.go(hid_type=HIDModes.BLE, ble_name='Flexible Determinist')

