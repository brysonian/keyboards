print("Starting BLE Flexible Determinist")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.col_pins = (board.A2, board.A3, board.D11, board.D12, board.D9)
keyboard.row_pins = (board.D5, board.D6, board.D10, board.D13, board.A5, board.A4, board.A1, board.A0)

# == LEFT == 
# qw**t
# yuio*
# asdfg
# kl'

# == RIGHT == 
# b*

keyboard.keymap = [[
  KC.Q, KC.W, KC.E, KC.R, KC.T,
  KC.A, KC.S, KC.D, KC.F, KC.G,
  KC.Z, KC.X, KC.C, KC.V, KC.B,
  KC.NO, KC.NO, KC.LSHIFT, KC.ENTER, KC.SPACE,
  KC.Y, KC.U, KC.I, KC.O, KC.P,  
  KC.H, KC.J, KC.K, KC.L, KC.QUOTE,  
  KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH,
  KC.SPACE, KC.BSPACE, KC.QUESTION, KC.NO, KC.NO
]]

if __name__ == '__main__':
    # keyboard.go()
    keyboard.go(hid_type=HIDModes.BLE, ble_name='BLE Flexible Determinist')

    yu