from cpkf.scan import mcp23017

addresses = [0x20, 0x21, 0x22, 0x23]

Scan = mcp23017.Scan(addresses)

def layout(kc1,  kc2,  kc3,  kc4,  kc5,     kc6, kc7, kc8, kc9, kc10,
           kc11, kc12, kc13, kc14, kc15,    kc16, kc17, kc18, kc19, kc20,
           kc21, kc22, kc23, kc24, kc25,    kc26, kc27, kc28, kc29, kc30,
           kc31, kc32, kc33, kc34, kc35,    kc36, kc37, kc38, kc39, kc40):
    return [ kc3, kc4, kc5, kc2, kc1, None, None, None,      kc21, kc22, kc23, kc24, kc25, None, None, None,
             kc15, kc14, kc13, kc12, kc11, None, None, None,      kc31, kc32, kc33, kc34, kc35, None, None, None,
             kc8, kc9, kc10, kc7, kc6, None, None, None,      kc26, kc27, kc28, kc29, kc30, None, None, None,
             kc20, kc19, kc18, kc17, kc16, None, None, None,      kc36, kc37, kc38, kc39, kc40, None, None, None  ]


def layouts(keymaps):
	physical_keymaps = []
	for keymap in keymaps :
		physical_keymaps.append(layout(*keymap))
	
	return physical_keymaps
