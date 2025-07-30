print("Starting BLE Flexible Determinist")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.col_pins = (board.A2, board.A3, board.D11, board.D12, board.D9)
keyboard.row_pins = (board.D5, board.D6, board.D10, board.D13, board.A5, board.A4, board.A1, board.A0)

keyboard.modules.append(Layers())
keyboard.modules.append(TapDance())

# ,,,,,,,,,,,,,,,,,,,,,,,,          

TO_ZERO = KC.TO(0)
TO_ONE = KC.TO(1)
SPACE_DOT = KC.TD(KC.SPACE, KC.DOT)

keyboard.keymap = [
  [
#╭──────────┬──────────┬──────────┬──────────┬──────────╮
#│    Q     │    W     │    E     │    R     │    T     │
    KC.Q,      KC.W,      KC.E,      KC.R,      KC.T,    
#├──────────┼──────────┼──────────┼──────────┼──────────┤
#│    A     │    S     │    D     │    F     │    G     │
    KC.A,      KC.S,      KC.D,      KC.F,      KC.G,
#├──────────┼──────────┼──────────┼──────────┼──────────┤
#│    Z     │    X     │    C     │    V     │    B     │
    KC.Z,       KC.X,      KC.C,     KC.V,       KC.B,   
#╰──────────┴──────────┼──────────┼──────────┼──────────┤
#                      │  LAYER   │  SHIFT   │  ENTER   │
    KC.NO,      KC.NO,    TO_ONE,   KC.LSHIFT, KC.ENTER,
#                      ╰──────────┴──────────┴──────────╯

# RIGHT MIRROR
#╭──────────┬──────────┬──────────┬──────────┬──────────╮
#│    P     │    O     │    I     │    U     │    Y     │
    KC.P,      KC.O,      KC.I,      KC.U,      KC.Y,    
#├──────────┼──────────┼──────────┼──────────┼──────────┤
#│    "     │    L     │    K     │    J     │    H     │
   KC.QUOTE,    KC.L,     KC.K,      KC.J,      KC.H,
#├──────────┼──────────┼──────────┼──────────┼──────────┤
#│    /     │    .     │     ,    │    M     │    N     │
   KC.SLASH,   KC.DOT,   KC.COMMA,   KC.M,      KC.N,   
#╰──────────┴──────────┼──────────┼──────────┼──────────┤
#                      │   TAB    │  BSPACE  │   SPACE  │
    KC.NO,     KC.NO,    KC.TAB.    KC.BSPACE, SPACE_DOT,
#                      ╰──────────┴──────────┴──────────╯
  ]
  # [
  #   KC.Q, KC.W, KC.E, KC.R, KC.T,
  #   KC.A, KC.S, KC.D, KC.F, KC.G,
  #   KC.Z, KC.X, KC.C, KC.V, KC.B,   
  #   KC.NO, KC.NO, TO_ONE, KC.LSHIFT, KC.ENTER,

  #   KC.P, KC.O, KC.I, KC.U, KC.Y,
  #   KC.QUOTE, KC.L, KC.K, KC.J, KC.H,
  #   KC.SLASH, KC.DOT, KC.COMMA, KC.M, KC.N,
  #   KC.NO, KC.NO, SPACE_DOT, KC.BSPACE, KC.TAB
  # ],
  [
    KC.LBRACKET, KC.N1, KC.N2, KC.N3, KC.RBRACKET,
    KC.SCOLON, KC.N4, KC.N5, KC.N6, KC.EQUAL,
    KC.GRAVE, KC.N7, KC.N8, KC.N9, KC.BSLASH,
    KC.NO, KC.NO, TO_ZERO, KC.N0, KC.TRANS,

    KC.NO, KC.NO, KC.UP, KC.PGUP, KC.PGDOWN,
    KC.NO, KC.RIGHT, KC.DOWN, KC.LEFT, KC.HOME,
    KC.NO, KC.NO, KC.NO, KC.NO, KC.END,
    KC.NO, KC.NO, KC.SPACE, KC.BSPACE, KC.NO
  ]
]

if __name__ == '__main__':
    # keyboard.go()
    keyboard.go(hid_type=HIDModes.BLE, ble_name='Flexible Determinist')
