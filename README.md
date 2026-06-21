| Supported Targets | ESP32 | ESP32-C2 | ESP32-C3 | ESP32-C5 | ESP32-C6 | ESP32-C61 | ESP32-H2 | ESP32-H21 | ESP32-H4 | ESP32-P4 | ESP32-S2 | ESP32-S3 | ESP32-S31 |
| ----------------- | ----- | -------- | -------- | -------- | -------- | --------- | -------- | --------- | -------- | -------- | -------- | -------- | --------- |

# UART Echo Example

(See the README.md file in the upper level 'examples' directory for more information about examples.)

This example demonstrates how to utilize UART interfaces by echoing back to the sender any data received on
configured UART.

## How to use example

### Hardware Required

The example can be run on any development board, that is based on the Espressif SoC. The board shall be connected to a computer with a single USB cable for flashing and monitoring. The external interface should have 3.3V outputs. You may
use e.g. 3.3V compatible USB-to-Serial dongle.

### Setup the Hardware

Connect the external serial interface to the board as follows.

```
  -----------------------------------------------------------------------------------------
  | Target chip Interface | Kconfig Option     | Default ESP Pin      | External UART Pin |
  | ----------------------|--------------------|----------------------|--------------------
  | Transmit Data (TxD)   | EXAMPLE_UART_TXD   | GPIO4                | RxD               |
  | Receive Data (RxD)    | EXAMPLE_UART_RXD   | GPIO5                | TxD               |
  | Ground                | n/a                | GND                  | GND               |
  -----------------------------------------------------------------------------------------
```
Note: Some GPIOs can not be used with certain chips because they are reserved for internal use. Please refer to UART documentation for selected target.

Optionally, you can set-up and use a serial interface that has RTS and CTS signals in order to verify that the
hardware control flow works. Connect the extra signals according to the following table, configure both extra pins in
the example code `uart_echo_example_main.c` by replacing existing `UART_PIN_NO_CHANGE` macros with the appropriate pin
numbers and configure UART1 driver to use the hardware flow control by setting `.flow_ctrl = UART_HW_FLOWCTRL_CTS_RTS`
and adding `.rx_flow_ctrl_thresh = 122` to the `uart_config` structure.

```
  ---------------------------------------------------------------
  | Target chip Interface | Macro           | External UART Pin |
  | ----------------------|-----------------|--------------------
  | Transmit Data (TxD)   | ECHO_TEST_RTS   | CTS               |
  | Receive Data (RxD)    | ECHO_TEST_CTS   | RTS               |
  | Ground                | n/a             | GND               |
  ---------------------------------------------------------------
```

### Configure the project

Use the command below to configure project using Kconfig menu as showed in the table above.
The default Kconfig values can be changed such as: EXAMPLE_TASK_STACK_SIZE, EXAMPLE_UART_BAUD_RATE, EXAMPLE_UART_PORT_NUM (Refer to Kconfig file).
```
idf.py menuconfig
```

### Build and Flash

Build the project and flash it to the board, then run monitor tool to view serial output:

```
idf.py -p PORT flash monitor
```

(To exit the serial monitor, type ``Ctrl-]``.)

See the Getting Started Guide for full steps to configure and use ESP-IDF to build projects.

## Example Output

Type some characters in the terminal connected to the external serial interface. As result you should see echo in the same terminal which you used for typing the characters. You can verify if the echo indeed comes from ESP board by
disconnecting either `TxD` or `RxD` pin: no characters will appear when typing.

## Troubleshooting

You are not supposed to see the echo in the terminal which is used for flashing and monitoring, but in the other UART configured through Kconfig can be used.


# HIL Docker Test Framework
Ovaj framework omogućava automatizovano testiranje UART integriteta između Raspberry Pi i ESP32 unutar Docker kontejnera.

## Preduslovi
- Docker instaliran na host sistemu (RPi).
- ESP32 povezan na `/dev/ttyS0`.

## Build imidža
```bash
docker build -t adi-hil-tester .

### 2. Čišćenje sistema: Zašto i kako?
**Zašto:** Docker prilikom bildovanja pravi "slojeve". Ako često menjaš `Dockerfile` ili instaliraš nove pakete, ostaju stari, neimenovani imidži (tzv. *dangling images*) koji troše dragoceni prostor na SD kartici tvog Raspberry Pi-ja. [Conversation History]

**Kako uraditi čišćenje (Staff Engineer komande):**

1.  **Uklanjanje neiskorišćenih imidža:**
    `docker image prune`
    *(Ovo će obrisati sve imidže koji nemaju ime/tag i ne koriste se).*
2.  **Generalno čišćenje (sve što nije aktivno):**
    `docker system prune`
    *(Obrisaće zaustavljene kontejnere, neiskorišćene mreže i dangling imidže).*
3.  **Provera zauzeća prostora:**
    `docker system df`
    *(Pokazuje ti tačno koliko Docker troši memorije na disku).*

### 3. Lista ključnih termina za sutrašnji intervju (InterVenture / TWINT)
Ovo su termini koje treba da "provučeš" kroz razgovor kako bi potvrdio svoj senioritet:

*   **HIL (Hardware-in-the-Loop):** Testiranje softvera na realnom hardveru, ne na simulatoru. [3]
*   **Containerization & Portability:** Pakovanje testova u Docker kako bi radili "bilo gde" bez zavisnosti od lokalnog Python-a. [2]
*   **Environment Parity:** Obezbeđivanje da je okruženje u kom pišeš testove isto kao ono u produkciji/CI-ju. [Conversation History]
*   **Deterministic Testing:** Testovi koji daju dosledne rezultate (poput onoga što si potvrdio dobijajući isti ishod unutar i van Docker-a). [Conversation History]
*   **Root-Cause Analysis:** Tvoja analiza da UART puca na 460.800 baud-a zbog fizičkog šuma, a ne greške u kodu. [4, 5, Conversation History]
*   **Scalable Test Design:** Korišćenje `@pytest.mark.parametrize` za automatsko generisanje matrice testova (različite brzine x različite dužine poruka). [93, Conversation History]
*   **CI/CD Ready:** Tvoj rad je spreman da se ubaci u Jenkins ili GitLab pipeline jer se pokreće jednom Docker komandom. [1, 2]
*   **Clean Code & Separation of Concerns:** Razdvajanje konfiguracije hardvera (`pytest.ini`) od logike testova. [260, Conversation History]
