import machine
import ssd1306
import time
from config import PINS, btn_up, btn_down, btn_ok, btn_back
from ui import Menu

# 1. Inicialização do Display (I2C)
i2c = machine.I2C(0, sda=machine.Pin(PINS["sda"]), scl=machine.Pin(PINS["scl"]))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# 2. Definição das funções do Menu
def start_sniffer():
    display.fill(0)
    display.text("Sniffing...", 0, 0)
    display.show()
    # Aqui entrará a lógica do CC1101 depois
    time.sleep(2)

def show_settings():
    display.fill(0)
    display.text("Configuracoes", 0, 0)
    display.show()
    time.sleep(2)

# 3. Configuração do Menu Principal
menu_items = ["Sniffer", "Replay", "Analyzer", "Settings"]
main_menu = Menu(display, menu_items)

# 4. Loop Principal de Navegação
print("Sistema Iniciado...")
main_menu.draw()

while True:
    if btn_up.value() == 0:
        main_menu.move_up()
        time.sleep(0.2) # Debounce
        
    if btn_down.value() == 0:
        main_menu.move_down()
        time.sleep(0.2) # Debounce
        
    if btn_ok.value() == 0:
        item_selecionado = menu_items[main_menu.index]
        if item_selecionado == "Sniffer":
            start_sniffer()
        elif item_selecionado == "Settings":
            show_settings()
        main_menu.draw() # Volta para o menu após sair da função
        time.sleep(0.2)
        
    if btn_back.value() == 0:
        # Lógica para voltar ou resetar
        main_menu.draw()
        time.sleep(0.2)
