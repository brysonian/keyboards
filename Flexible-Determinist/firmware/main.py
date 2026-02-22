# type: ignore[reportMissingImports]

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
from kmk.modules.tapdance import TapDance
from kmk.modules.macros import Macros


# SETUP THE MATRIX
keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.col_pins = (board.SCK, board.A3, board.D11, board.D12, board.D9)
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

# More tools
keyboard.modules.append(HoldTap())
tapdance = TapDance()
tapdance.tap_time = 750
keyboard.modules.append(tapdance)

keyboard.modules.append(Macros())

# CHORDS
SUPER_TAB = KC.HT(KC.TAB, KC.LGUI(KC.GRAVE), tap_time=150)
combos = Combos()
combos.combos = [
    Chord((KC.BKDL, KC.SPACE), KC.LEFT, timeout=100),
    Chord((SUPER_TAB, KC.SPACE), KC.RIGHT, timeout=100),
]
keyboard.modules.append(combos)



# KEYMAP
 
keyboard.keymap = [
#                                          ALPHA LAYER
[
KC.TD(KC.Q, KC.ESC),    KC.W,                  KC.E,                 KC.R,                 KC.T, KC.Y,  KC.U,                 KC.I,                 KC.O,                  KC.P,
KC.A,                   KC.HT(KC.S, KC.LCTRL), KC.HT(KC.D, KC.LALT), KC.HT(KC.F, KC.LGUI), KC.G, KC.H,  KC.HT(KC.J, KC.LGUI), KC.HT(KC.K, KC.LALT), KC.HT(KC.L, KC.LCTRL), KC.QUOTE,
KC.HT(KC.Z, KC.LSHIFT), KC.X,                  KC.C,                 KC.V,                 KC.B, KC.N,  KC.M,                 KC.COMMA,             KC.DOT,                KC.HT(KC.SLASH, KC.RSHIFT),
                    
                    TO_NUM,    TO_MOVE,  KC.ENTER,           KC.SPACE,   KC.BKDL,  SUPER_TAB
],

#                                           NUM LAYER
[
_____,    _____,    _____,    KC.LBRC,    KC.RBRC,           KC.N1,      KC.N2,    KC.N3,      KC.N0,      KC.BSLASH,
_____,    KC.LCTRL, KC.LALT,  KC.LGUI,    _____,             KC.N4,      KC.N5,    KC.N6,      KC.EQL,     KC.SCOLON,
KC.LSHIFT,_____,    _____,    _____,      KC.TAB,            KC.N7,      KC.N8,    KC.N9,      KC.MINS,    KC.SLASH,    
                      
                      TO_ALPHA,    TO_MOVE,  KC.LSHIFT,      _____,      KC.BKDL,_____
],


#                                           MOVE LAYER
[
KC.BLE_REFRESH,  KC.BLE_DISCONNECT, _____,   _____,     _____,            _____,    KC.LALT(KC.LEFT),   KC.UP,     KC.LALT(KC.RIGHT), _____,
KC.HID_SWITCH,   KC.LCTRL,          KC.LALT, KC.LGUI,   _____,            _____,    KC.LEFT,            KC.DOWN,   KC.RIGHT,          _____,
_____,           _____,             _____,   _____,     _____,            _____,    KC.HOME,            KC.PGDOWN, KC.END,            _____,

                                 TO_NUM,   TO_ALPHA,   KC.LSHIFT,         _____,   KC.BKDL,    _____
],
]


if __name__ == '__main__':
   keyboard.go(
     hid_type=HIDModes.BLE,
     secondary_hid_type=HIDModes.USB,
     ble_name='FlxDet'
    )

