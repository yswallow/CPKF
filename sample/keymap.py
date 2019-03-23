from adafruit_hid.keycode import Keycode as KC
from cpkf.key_object import LT, LO, MD, S, MO
from cpkf.consumer_control import VOLU, VOLD

L_LOWER = 1 
L_RAISE = 2
L_ARROW = 3
L_ADJUST= 4

def layout(kc1,  kc2,  kc3,  kc4,  kc5,     kc6, kc7, kc8, kc9, kc10,
           kc11, kc12, kc13, kc14, kc15,    kc16, kc17, kc18, kc19, kc20,
           kc21, kc22, kc23, kc24, kc25,    kc26, kc27, kc28, kc29, kc30,
           kc31, kc32, kc33, kc34, kc35,    kc36, kc37, kc38, kc39, kc40):
    return [ kc3, kc4, kc5, kc2, kc1, None, None, None,      kc21, kc22, kc23, kc24, kc25, None, None, None,
             kc15, kc14, kc13, kc12, kc11, None, None, None,      kc31, kc32, kc33, kc34, kc35, None, None, None,
             kc8, kc9, kc10, kc7, kc6, None, None, None,      kc26, kc27, kc28, kc29, kc30, None, None, None,
             kc20, kc19, kc18, kc17, kc16, None, None, None,      kc36, kc37, kc38, kc39, kc40, None, None, None  ]

keymap = [ layout(
            LO(KC.Q, KC.LEFT_ALT), KC.MINUS, KC.COMMA, KC.PERIOD, KC.W,
                KC.M, KC.Y, KC.K, KC.R, LO(KC.P, KC.RIGHT_ALT),
            LO(KC.A, KC.LEFT_CONTROL), KC.O, KC.E, KC.I, KC.U,
                KC.N, KC.H, KC.J, KC.L, LO(KC.G, KC.RIGHT_CONTROL),
            LO(KC.Z, KC.LEFT_SHIFT), KC.X, KC.C, KC.V, KC.F,
                KC.S, KC.T, KC.D, KC.B, LO(KC.ENTER, KC.RIGHT_SHIFT),
            LO(KC.ESCAPE, KC.LEFT_CONTROL), KC.GUI, LT(L_ARROW, KC.F10), LT(L_LOWER, KC.TAB), LT(L_LOWER, KC.SPACE),
                LT(L_RAISE, KC.ENTER), KC.BACKSPACE, MD(KC.CONTROL, KC.SPACE), KC.RIGHT_GUI, KC.RIGHT_ALT
            ),
            
            #lower = 1
            layout(
                S(KC.ONE), S(KC.TWO), S(KC.THREE), S(KC.FOUR), S(KC.FIVE),
                    S(KC.SIX), S(KC.SEVEN), S(KC.EIGHT), S(KC.NINE), S(KC.ZERO),
                KC.ONE, KC.TWO, KC.THREE, KC.FOUR, KC.FIVE,
                    KC.SIX, KC.SEVEN, KC.EIGHT, KC.NINE, KC.ZERO,
                None, None, None, None, None, 
                    None, None, None, None, None, 
                None, None, None, None, None, 
                    MO(L_ADJUST), KC.DELETE, S(KC.DELETE), None, None
            ),
            
            #raise = 2
            layout(
                None, None, S(KC.GRAVE_ACCENT), S(KC.EQUALS), S(KC.LEFT_BRACKET),
                    S(KC.RIGHT_BRACKET), S(KC.SEMICOLON), S(KC.QUOTE), S(KC.FORWARD_SLASH), S(KC.BACKSLASH),
                None, None, KC.GRAVE_ACCENT, KC.EQUALS, KC.LEFT_BRACKET,
                    KC.RIGHT_BRACKET, KC.SEMICOLON, KC.QUOTE, KC.FORWARD_SLASH, KC.BACKSLASH,
                None, None, None, None, None, 
                    None, None, None, None, None, 
                None, None, None, None, MO(L_ADJUST), 
                    None, None, None, None, None
            ),
            
            #arrow = 3
            layout(
                None, KC.F1, KC.F2, KC.F3, KC.F4,
                    MD(KC.ALT, KC.LEFT_ARROW), None, KC.UP_ARROW, None, None, 
                None, KC.F5, KC.F6, KC.F7, KC.F8,
                    None, KC.LEFT_ARROW, KC.DOWN_ARROW, KC.RIGHT_ARROW, None,
                None, KC.F9, KC.F10, KC.F11, KC.F12,
                    KC.HOME, KC.PAGE_DOWN, KC.PAGE_UP, KC.END, None, 
                None, None, None, None, None, 
                    None, None, None, None, None
            ),
            
            #adjust = 4
            layout(
                None, None, None, None, None,
                    None, None, KC.PRINT_SCREEN, VOLU(), None,
                None, None, None, None, None,
                    None, None, None, VOLD(), None,
                None, None, None, None, None,
                    None, None, None, None, None,
                None, None, None, None, None,
                    None, None, None, None, None
            ),
            
            layout(
                None, None, None, None, None,
                    None, None, None, None, None,
                None, None, None, None, None,
                    None, None, None, None, None,
                None, None, None, None, None,
                    None, None, None, None, None,
                None, None, None, None, None,
                    None, None, None, None, None
            )
         ]
