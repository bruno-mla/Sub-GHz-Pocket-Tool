from machine import Pin

# Mapeamento de Pinos para Raspberry Pi Pico
PINS = {
    "sda": 26, "scl": 27,    # I2C1
    "sck": 18, "miso": 16,   # SPI0
    "mosi": 19, "cs": 17,    # SPI0
    "gdo0": 15,              # Interrupção Rádio
    "up": 2, "down": 3,      # Botões
    "ok": 6, "back": 7       # Botões
}

def setup_button(gpio):
    # No Pico, o Pull-up interno é essencial para botões ligados ao GND
    return Pin(gpio, Pin.IN, Pin.PULL_UP)

# Inicializa os botões para uso no main.py
btn_up = setup_button(PINS["up"])
btn_down = setup_button(PINS["down"])
btn_ok = setup_button(PINS["ok"])
btn_back = setup_button(PINS["back"])
