# ESP32-C3 Super Mini Setup ⚡

Esta versão utiliza o ESP32-C3 Super Mini, focado em compacidade e conectividade Wi-Fi/Bluetooth. Por possuir um número limitado de GPIOs, a pinagem foi otimizada para suportar o rádio CC1101, o display OLED e os 4 botões de navegação.

## 📌 Pinagem (GPIO Map)

| Componente | Pino ESP32-C3 | Função |
| :--- | :--- | :--- |
| **OLED SDA** | GPIO 8 | I2C Data |
| **OLED SCL** | GPIO 9 | I2C Clock |
| **CC1101 SCK** | GPIO 4 | SPI Clock |
| **CC1101 MISO**| GPIO 5 | SPI MISO |
| **CC1101 MOSI**| GPIO 6 | SPI MOSI |
| **CC1101 CS** | GPIO 7 | SPI Chip Select |
| **CC1101 GDO0**| GPIO 10| Packet Interrupt |
| **Button UP** | GPIO 0 | Pull-up Interno |
| **Button DOWN**| GPIO 1 | Pull-up Interno |
| **Button OK** | GPIO 2 | Pull-up Interno |
| **Button BACK**| GPIO 3 | Pull-up Interno |

## 🛠️ Observações de Montagem
- **Alimentação:** Utilize o pino de 3.3V do ESP32 para o CC1101 e o OLED. O CC1101 é sensível a tensões superiores.
- **Botões:** Os botões devem ser ligados entre o GPIO correspondente e o **GND**. O código utiliza resistores de Pull-up internos para simplificar o circuito.
- **Antena:** Certifique-se de que a antena do CC1101 esteja conectada antes de realizar testes de transmissão para evitar danos ao módulo.

## 🚀 Instalação
1. Grave o firmware MicroPython específico para ESP32-C3.
2. Utilize o Thonny IDE para transferir os arquivos das pastas `/src/common` e `/src/esp32c3`.
