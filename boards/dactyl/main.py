from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()

# TODO Comment one of these on each side
split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(split_type=SplitType.UART, split_flip=True,)

layers_ext = Layers()
modtap = ModTap()

keyboard.modules = [layers_ext, split, modtap]
keyboard.extensions = []
#
# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.LT(3, KC.SPC)
LSFT_ESC = KC.MT(KC.ESC, KC.LSFT)
LCTL_BKS = KC.MT(KC.BKSP, KC.LCTL)
LALT_SPC = KC.MT(KC.SPC, KC.LALT)

keyboard.keymap = [
    [  # QWERTY
          KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                          KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,
          KC.A,     KC.S,     KC.D,     KC.F,     KC.G,                          KC.H,     KC.J,     KC.K,     KC.L,  KC.SCLN,
          KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,                          KC.N,     KC.M,  KC.COMM,   KC.DOT,  KC.SLSH,
                   LOWER,    RAISE,                                                               XXXXXXX,  XXXXXXX,
                                    LSFT_ESC, LCTL_BKS, LALT_SPC,   XXXXXXX,  XXXXXXX,  XXXXXXX,
                                                 RAISE,  KC.LGUI,   XXXXXXX,    LOWER,
    ],
    [  # LOWER
       XXXXXXX,    KC.N7,    KC.N8,    KC.N9,  XXXXXXX,                       XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
       XXXXXXX,    KC.N4,    KC.N5,    KC.N6,  XXXXXXX,                       XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
       XXXXXXX,    KC.N1,    KC.N2,    KC.N3,  XXXXXXX,                       XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                 XXXXXXX,    KC.N0,                                                               XXXXXXX,  XXXXXXX,
                                     XXXXXXX,  XXXXXXX,  XXXXXXX,   XXXXXXX,  XXXXXXX,  XXXXXXX,
                                               XXXXXXX,  XXXXXXX,   XXXXXXX,  XXXXXXX,
    ],
    [  # LOWER
       XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                       XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
       XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                       XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
       XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                       XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                 XXXXXXX,  XXXXXXX,                                                              XXXXXXX,  XXXXXXX,
                                     XXXXXXX,  XXXXXXX,  XXXXXXX,   XXXXXXX,  XXXXXXX,  XXXXXXX,
                                               XXXXXXX,  XXXXXXX,   XXXXXXX,  XXXXXXX,
    ],
]

if __name__ == '__main__':
    keyboard.go()
