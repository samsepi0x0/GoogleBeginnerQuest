global_pin = 0

def gpio_set_mask(mask):
    global global_pin
    global_pin |= mask

def gpio_clr_mask(mask):
    global global_pin
    global_pin &= ~mask

gpio_set_mask(67)
gpio_clr_mask(0)
print(chr(global_pin), end='')
gpio_set_mask(20)
gpio_clr_mask(3)
print(chr(global_pin), end='')
gpio_set_mask(2)
gpio_clr_mask(16)
print(chr(global_pin), end='')
gpio_set_mask(57)
gpio_clr_mask(4)
print(chr(global_pin), end='')
gpio_set_mask(0)
gpio_clr_mask(25)
print(chr(global_pin), end='')
gpio_set_mask(5)
gpio_clr_mask(2)
print(chr(global_pin), end='')
gpio_set_mask(18)
gpio_clr_mask(65)
print(chr(global_pin), end='')
gpio_set_mask(1)
gpio_clr_mask(2)
print(chr(global_pin), end='')
gpio_set_mask(64)
gpio_clr_mask(17)
print(chr(global_pin), end='')
gpio_set_mask(2)
gpio_clr_mask(0)
print(chr(global_pin), end='')
gpio_set_mask(1)
gpio_clr_mask(6)
print(chr(global_pin), end='')
gpio_set_mask(18)
gpio_clr_mask(65)
print(chr(global_pin), end='')
gpio_set_mask(1)
gpio_clr_mask(0)
print(chr(global_pin), end='')
gpio_set_mask(4)
gpio_clr_mask(2)
print(chr(global_pin), end='')
gpio_set_mask(0)
gpio_clr_mask(0)
print(chr(global_pin), end='')
gpio_set_mask(64)
gpio_clr_mask(16)
print(chr(global_pin), end='')
gpio_set_mask(16)
gpio_clr_mask(64)
print(chr(global_pin), end='')
gpio_set_mask(2)
gpio_clr_mask(4)
print(chr(global_pin), end='')
gpio_set_mask(0)
gpio_clr_mask(3)
print(chr(global_pin), end='')
gpio_set_mask(9)
gpio_clr_mask(0)
print(chr(global_pin), end='')
gpio_set_mask(0)
gpio_clr_mask(1)
print(chr(global_pin), end='')
gpio_set_mask(0)
gpio_clr_mask(8)
print(chr(global_pin), end='')
gpio_set_mask(8)
gpio_clr_mask(0)
print(chr(global_pin), end='')
gpio_set_mask(65)
gpio_clr_mask(24)
print(chr(global_pin), end='')
gpio_set_mask(22)
gpio_clr_mask(64)
print(chr(global_pin), end='')
gpio_set_mask(0)
gpio_clr_mask(0)
print(chr(global_pin), end='')
gpio_set_mask(0)
gpio_clr_mask(5)
print(chr(global_pin), end='')
gpio_set_mask(0)
gpio_clr_mask(2)
print(chr(global_pin), end='')
gpio_set_mask(65)
gpio_clr_mask(16)
print(chr(global_pin), end='')
gpio_set_mask(22)
gpio_clr_mask(65)
print(chr(global_pin), end='')
gpio_set_mask(1)
gpio_clr_mask(6)
print(chr(global_pin), end='')
gpio_set_mask(4)
gpio_clr_mask(0)
print(chr(global_pin), end='')
gpio_set_mask(66)
gpio_clr_mask(21)
print(chr(global_pin), end='')
gpio_set_mask(1)
gpio_clr_mask(0)
print(chr(global_pin), end='')
gpio_set_mask(0)
gpio_clr_mask(2)
print(chr(global_pin), end='')
gpio_set_mask(24)
gpio_clr_mask(65)
print(chr(global_pin), end='')
gpio_set_mask(67)
gpio_clr_mask(24)
print(chr(global_pin), end='')
gpio_set_mask(24)
gpio_clr_mask(67)
print(chr(global_pin), end='')
gpio_set_mask(2)
gpio_clr_mask(8)
print(chr(global_pin), end='')
gpio_set_mask(65)
gpio_clr_mask(18)
print(chr(global_pin), end='')
gpio_set_mask(16)
gpio_clr_mask(64)
print(chr(global_pin), end='')
gpio_set_mask(2)
gpio_clr_mask(0)
print(chr(global_pin), end='')
gpio_set_mask(68)
gpio_clr_mask(19)
print(chr(global_pin), end='')
gpio_set_mask(19)
gpio_clr_mask(64)
print(chr(global_pin), end='')
gpio_set_mask(72)
gpio_clr_mask(2)
print(chr(global_pin), end='')
gpio_set_mask(2)
gpio_clr_mask(117)
print(chr(global_pin), end='')