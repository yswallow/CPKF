from cpkf.scan import matrix_scan
import board

col_pins = [board.P1_13, board.P1_15, board.P0_02, board.P0_29, board.P0_31, board.P0_26, board.P0_04, board.P0_06, board.P0_08, board.P1_09]
row_pins = [board.P1_00, board.P0_24, board.P0_22, board.P0_20 ]

Scan = matrix_scan.Scan(row_pins, col_pins, row2col=False)

def layout(kc1,  kc2,  kc3,  kc4,  kc5,     kc6, kc7, kc8, kc9, kc10,
           kc11, kc12, kc13, kc14, kc15,    kc16, kc17, kc18, kc19, kc20,
           kc21, kc22, kc23, kc24, kc25,    kc26, kc27, kc28, kc29, kc30,
           kc31, kc32, kc33, kc34, kc35,    kc36, kc37, kc38, kc39, kc40):
    return [ kc1,  kc2,  kc3,  kc4,  kc5,     kc6, kc7, kc8, kc9, kc10,
           kc11, kc12, kc13, kc14, kc15,    kc16, kc17, kc18, kc19, kc20,
           kc21, kc22, kc23, kc24, kc25,    kc26, kc27, kc28, kc29, kc30,
           kc31, kc32, kc33, kc34, kc35,    kc36, kc37, kc38, kc39, kc40 ]

def layouts(keymaps):
	physical_keymaps = []
	for keymap in keymaps :
		physical_keymaps.append(layout(*keymap))
	
	return physical_keymaps
