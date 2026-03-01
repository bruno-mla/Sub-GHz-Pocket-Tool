# Raspberry Pi Pico Setup 🍓

Esta versão utiliza o Raspberry Pi Pico (ou Pico W) como cérebro do dispositivo. O Pico oferece mais pinos GPIO, facilitando futuras expansões.

## 🔧 Conexões
Siga a tabela de pinagem abaixo para conectar os módulos. Recomenda-se o uso de headers fêmea para manter a modularidade.

## 📌 Pinagem (GPIO Map)

| Componente | Pino Pico (GP) | Função |
| :--- | :--- | :--- |
| **OLED SDA** | GP26 | I2C Data (I2C1) |
| **OLED SCL** | GP27 | I2C Clock (I2C1) |
| **CC1101 SCK** | GP18 | SPI Clock (SPI0) |
| **CC1101 MISO**| GP16 | SPI MISO (SPI0) |
| **CC1101 MOSI**| GP19 | SPI MOSI (SPI0) |
| **CC1101 CS** | GP17 | SPI Chip Select |
| **CC1101 GDO0**| GP15 | Interrupção (GDO0) |
| **Button UP** | GP2  | Pull-up Interno |
| **Button DOWN**| GP3  | Pull-up Interno |
| **Button OK** | GP6  | Pull-up Interno |
| **Button BACK**| GP7  | Pull-up Interno |

## 🚀 Instalação do Firmware
1. Baixe o firmware MicroPython `.uf2` mais recente para o Pico.
2. Conecte o Pico ao computador segurando o botão `BOOTSEL`.
3. Arraste o arquivo para a unidade que aparecer.

4. Carregue os arquivos da pasta `/src/common` e `/src/pico` para a raiz do dispositivo.
