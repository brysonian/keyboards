# type: ignore[reportMissingImports]

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes
from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.modules.layers import Layers
# from kmk.modules.combos import Combos, Chord
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
  val_limit=100,
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
    elif layer == 1:
      rgb.set_hsv_fill(195, 255, 1)
      rgb.show()
    else:
      rgb.set_hsv_fill(100, 255, 1)
      rgb.show()

  def deactivate_layer(self, keyboard, layer):
    super().deactivate_layer(keyboard, layer)
    rgb.set_hsv_fill(0, 0, 0)
    rgb.show()


keyboard.modules.append(RGBLayers())
TO_ALPHA = KC.MO(0)
TO_NUM = KC.MO(1)
TO_MOVE = KC.MO(2)

# MACROS
DELETE_WORD = KC.LALT(KC.BSPACE)
WORD_LEFT = KC.LALT(KC.LEFT)
WORD_RIGHT = KC.LALT(KC.RIGHT)

# CHORDS
# combos = Combos()
# combos.combos = [
#     Chord((KC.LSHIFT, KC.SPACE), KC.TAB, timeout=100),
# ]
# keyboard.modules.append(combos)

# HOLD
keyboard.modules.append(HoldTap())
HOLD_Q_ESC = KC.HT(KC.Z, KC.ESC)
HOLD_Z_SHIFT = KC.HT(KC.Z, KC.LSHIFT)
HOLD_SLASH_SHIFT = KC.HT(KC.SLASH, KC.RSHIFT)
HOLD_BSPACE_DELWORD = KC.HT(KC.BSPACE, DELETE_WORD)

HOLD_S_LCTRL = KC.HT(KC.S, KC.LCTRL)
HOLD_D_LALT = KC.HT(KC.D, KC.LALT)
HOLD_F_LGUI = KC.HT(KC.F, KC.LGUI)

HOLD_J_LGUI = KC.HT(KC.J, KC.LGUI)
HOLD_K_LALT = KC.HT(KC.K, KC.LALT)
HOLD_L_LCTRL = KC.HT(KC.L, KC.LCTRL)

# KEYMAP

keyboard.keymap = [
#                                          ALPHA LAYER
[
HOLD_Q_ESC,   KC.W,         KC.E,         KC.R,         KC.T,           KC.Y,  KC.U,        KC.I,         KC.O,           KC.P,
KC.A,         HOLD_S_LCTRL, HOLD_D_LALT,  HOLD_F_LGUI,  KC.G,           KC.H,  HOLD_J_LGUI, HOLD_K_LALT,  HOLD_L_LCTRL,   KC.QUOTE,
HOLD_Z_SHIFT, KC.X,         KC.C,         KC.V,         KC.B,           KC.N,  KC.M,        KC.COMMA,     KC.DOT,         HOLD_SLASH_SHIFT,
                    
                    TO_NUM,    TO_MOVE,  KC.ENTER,           KC.SPACE,   HOLD_BSPACE_DELWORD,  KC.TAB
],

#                                           NUM LAYER
[
_____,    _____,    _____,    KC.LBRC,    KC.RBRC,           KC.N1,      KC.N2,    KC.N3,      KC.N0,      KC.BSLASH,
_____,    KC.LCTRL, KC.LALT,  KC.LGUI,    _____,             KC.N4,      KC.N5,    KC.N6,      KC.EQL,     KC.SCOLON,
KC.LSHIFT,_____,    _____,    _____,      KC.TAB,            KC.N7,      KC.N8,    KC.N9,      KC.MINS,    KC.SLASH,    
                      
                      TO_ALPHA,    TO_MOVE,  KC.LSHIFT,      _____,      KC.BSPACE,_____
],


#                                           MOVE LAYER
[
KC.BLE_REFRESH,  KC.BLE_DISCONNECT, _____,   _____,     _____,            _____,    WORD_LEFT,   KC.UP,     WORD_RIGHT,   _____,
KC.HID_SWITCH,   KC.LCTRL,          KC.LALT, KC.LGUI,   _____,            _____,    KC.LEFT,     KC.DOWN,   KC.RIGHT,     _____,
_____,           _____,             _____,   _____,     _____,            _____,    KC.HOME,     KC.PGDOWN, KC.END,       _____,

                                 TO_NUM,   TO_ALPHA,   KC.LSHIFT,        _____,   KC.BSPACE,    _____
],
]


if __name__ == '__main__':
   keyboard.go(
     hid_type=HIDModes.BLE,
     secondary_hid_type=HIDModes.USB,
     ble_name='FlxDet'
    )

  #  keyboard.go(
  #    hid_type=HIDModes.USB,
  #    secondary_hid_type=HIDModes.BLE
  #   )
#   keyboard.go()
