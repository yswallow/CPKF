from adafruit_hid.keycode import Keycode as KC
from cpkf.key_object import LO, LT, C, S, MO, Alt
from cpkf.keycode_jp import KeycodeJP as JP
from cpkf.consumer_control import VOLD, VOLU
from cpkf.mousekey import MOUSEU, MOUSED, MOUSEL, MOUSER, WHEELU, WHEELD, MOUSELB
from cpkf.bluetooth_object import BT_EN, USB_EN

L_LOWER = 1 
L_RAISE = 2
L_ARROW = 3
L_ADJUST= 4
L_MOUSE = 5

keymap = [ [
            LO(KC.Q, KC.LEFT_ALT), KC.W, KC.E, KC.R, KC.T,
                KC.Y, KC.U, KC.I, KC.O, LO(KC.P, KC.RIGHT_ALT),
            LO(KC.A, KC.LEFT_CONTROL), KC.S, KC.D, KC.F, KC.G,
                KC.H, KC.J, KC.K, KC.L, LO(KC.MINUS, KC.RIGHT_CONTROL),
            LO(KC.Z, KC.LEFT_SHIFT), KC.X, KC.C, KC.V, KC.B,
                KC.N, KC.M, KC.COMMA, KC.PERIOD, LO(KC.ENTER, KC.RIGHT_SHIFT),
            LO(KC.ESCAPE, KC.LEFT_CONTROL), KC.GUI, LT(L_ARROW, KC.F10), LT(L_LOWER, KC.TAB), LT(L_LOWER, KC.SPACE),
                LT(L_RAISE, KC.ENTER), KC.BACKSPACE, C(KC.SPACE), KC.RIGHT_GUI, KC.RIGHT_ALT
            ],
            
            #lower = 1
            [
                S(KC.ONE), S(KC.TWO), S(KC.THREE), S(KC.FOUR), S(KC.FIVE),
                    S(KC.SIX), S(KC.SEVEN), S(KC.EIGHT), S(KC.NINE), S(KC.ZERO),
                KC.ONE, KC.TWO, KC.THREE, KC.FOUR, KC.FIVE,
                    KC.SIX, KC.SEVEN, KC.EIGHT, KC.NINE, KC.ZERO,
                MO(L_MOUSE), None, None, None, None, 
                    None, None, None, None, None, 
                None, None, None, None, None, 
                    MO(L_ADJUST), KC.DELETE, S(KC.DELETE), None, None
            ],
            
            #raise = 2
            [
                JP.BACK_SLASH, JP.PIPE, S(KC.GRAVE_ACCENT), S(KC.EQUALS), S(KC.LEFT_BRACKET),
                    S(KC.RIGHT_BRACKET), S(KC.SEMICOLON), S(KC.QUOTE), S(KC.FORWARD_SLASH), S(KC.BACKSLASH),
                JP.UNDERBAR, JP.JPYEN, KC.GRAVE_ACCENT, KC.EQUALS, KC.LEFT_BRACKET,
                    KC.RIGHT_BRACKET, KC.SEMICOLON, KC.QUOTE, KC.FORWARD_SLASH, KC.BACKSLASH,
                None, None, None, None, None, 
                    None, None, None, None, None, 
                None, None, None, None, MO(L_ADJUST), 
                    None, None, None, None, None
            ],
            
            #arrow = 3
            [
                None, KC.F1, KC.F2, KC.F3, KC.F4,
                    Alt(KC.LEFT_ARROW), None, KC.UP_ARROW, None, None, 
                None, KC.F5, KC.F6, KC.F7, KC.F8,
                    KC.LEFT_ARROW, KC.LEFT_ARROW, KC.DOWN_ARROW, KC.RIGHT_ARROW, None,
                KC.LEFT_SHIFT, KC.F9, KC.F10, KC.F11, KC.F12,
                    KC.HOME, KC.PAGE_DOWN, KC.PAGE_UP, KC.END, None, 
                None, None, None, None, None, 
                    None, None, None, None, None
            ],
            
            #adjust = 4
            [
                BT_EN(), None, None, None, None,
                    None, None, KC.PRINT_SCREEN, VOLU(), USB_EN(),
                None, None, None, None, None,
                    None, None, None, None, None,
                None, None, None, None, None,
                    None, None, None, VOLD(), None,
                None, None, None, None, None,
                    None, None, None, None, None
            ],
            # mouse = 5
            [
                None, None, None, None, None,
                    WHEELU(), MOUSEU(), MOUSEU(), None, None,
                None, None, None, None, None,
                    MOUSEL(), MOUSEL(), MOUSED(), MOUSER(), None,
                None, None, None, None, None,
                    WHEELD(), None, None, None, None,
                None, None, None, None, None,
                    MOUSELB(), None, None, None, None
            ]
         ]