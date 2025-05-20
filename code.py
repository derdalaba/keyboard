print("Starting")
NUM_LEDS = 11

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.international import International

keyboard = KMKKeyboard()

from kmk.extensions.RGB import RGB

#rgb = RGB(pixel_pin = board.GP15, num_pixels = NUM_LEDS, animation_mode = 4, breathe_center = 1.5, val_limit = 35)
#keyboard.extensions.append(rgb)

keyboard.extensions.append(International())

keyboard.col_pins = (board.GP20, board.GP19, board.GP18, board.GP17, board.GP16, board.GP4, board.GP3, board.GP2, board.GP1, board.GP0,)
keyboard.row_pins = ( board.GP5, board.GP6, board.GP7, board.GP8,board.GP9,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())             

LAYER_TAP = KC.LT(1, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=250)
LAYER_TAP2 = KC.LT(1, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=250)
LAYER_TAP3 = KC.LT(2, KC.G, prefer_hold=True, tap_interrupted=False, tap_time=250)
keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T,                    KC.Y, KC.U, KC.I, KC.O, KC.P,
        KC.A, KC.S, KC.D, KC.F, KC.G,                    KC.H, KC.J, KC.K, KC.L, KC.SCLN,
        KC.Z, KC.X, KC.C, KC.V, KC.B,                    KC.N, KC.M, KC.COMM, KC.DOT, KC.LCTL,
        LAYER_TAP, KC.LBRC, KC.RBRC, KC.BSLS, KC.LSHIFT, KC.BSPACE, KC.GRV, KC.SLASH, KC.QUOT,KC.LALT,
        KC.TAB, KC.LCTRL, KC.LALT, KC.ENT, KC.SPACE,           LAYER_TAP2, KC.F4, KC.F5, KC.F12,KC.RALT,
        
    ],
       #     KC.Q, KC.W, KC.E, KC.R, KC.T,    KC.Y, KC.U, KC.I, KC.O, KC.P,
       # KC.A, KC.S, KC.D, KC.F, KC.G,    KC.H, KC.J, KC.K, KC.L, KC.SCLN,
       # KC.Z, KC.X, KC.C, KC.V, KC.B,    KC.N, KC.M, KC.COMM, KC.DOT, KC.LCTL,
       # LAYER_TAP, KC.LBRC, KC.RBRC, KC.BSLS, KC.SPACE, KC.BSPACE, KC.GRV, KC.SLASH, KC.QUOT,KC.LALT,
       # KC.TAB, KC.NO, KC.NO, KC.NO, KC.LSHIFT, LAYER_TAP2, KC.NO, KC.NO, KC.NO,KC.RALT,  
    [
        KC.F2,  KC.N1,  KC.N2, KC.N3,  KC.F12,         KC.F1, KC.F3, KC.F4, KC.F6, KC.F7,
        KC.N1, KC.N4, KC.N5, KC.N6, KC.TRNS,          KC.F8, KC.F9, KC.F10, KC.F11, KC.TRNS,
        KC.NUBS, KC.N7, KC.N8, KC.N9, KC.MINS,        KC.EQL,KC.TRNS, KC.UP, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.N0, KC.LGUI, KC.TRNS,  KC.TRNS, KC.LEFT, KC.DOWN, KC.RIGHT, KC.TRNS,
        KC.LCTL, KC.TRNS, KC.TRNS, KC.TRNS, KC.BSPACE,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        
    ],
    [
        KC.TRNS, KC.N1,  KC.N2, KC.N3, KC.TRNS,         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.N4, KC.N5, KC.N6, KC.TRNS,          KC.TRNS, KC.LEFT, KC.TRNS, KC.RIGHT, KC.TRNS,
        KC.TRNS, KC.N7, KC.N8, KC.N9, KC.TRNS,          KC.EQL,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.N0, KC.LGUI, KC.BSPACE,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        
    ]
    #[
        #KC.NO, KC.Q, KC.W, KC.E, KC.R,
        #KC.LSHIFT, KC.A, KC.S, KC.D, KC.SPACE,
        #KC.LCTRL, KC.Y, KC.X, KC.C, KC.TAB
    #]
]

if __name__ == '__main__':
    keyboard.go()




