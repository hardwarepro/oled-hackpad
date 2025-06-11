import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

encoder = EncoderHandler()
keyboard.modules.append(encoder)


PINS = [board.D3, board.D4, board.D2, board.D1]

# Set up the key scanner
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# defining my key matrix
keyboard.keymap = [
    [
        # key 1 opens gmail.com
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.L),
            Release(KC.LCTRL),
            KC.MACRO("gmail.com"),
            Tap(KC.ENTER)
        ),

        # key 2 takes a screenshot (for windows only)
        KC.MACRO(
            Press(KC.LGUI),
            Press(KC.LSHIFT),
            Tap(KC.S),
            Release(KC.LSHIFT),
            Release(KC.LGUI),
        ),

        # key 3 hold down shift
        KC.MACRO(
            Press(KC.LSHIFT)
        ),

        # key 4 does control + S
        KC.MACRO(
            Press(KC.LCTRL),
            Tap(KC.S),
            Release(KC.LCTRL),
        ),
    ]
]


# Rotate left is volume down, and rotate right is volume up
encoder.map = [
    ((KC.VOLD, KC.VOLU),)  # volume control stuff
]

if __name__ == '__main__':
    keyboard.go()