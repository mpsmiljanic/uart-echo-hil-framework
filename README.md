# Containerized HIL UART Integrity Framework

## Overview

This project is a professional Hardware-in-the-Loop (HIL) testing framework designed to validate UART communication stability and signal integrity between a Raspberry Pi 3B+ and an ESP32-S3.

## Key Features

### Modular Test Architecture
Separation of infrastructure (`conftest.py`), configuration (`pytest.ini`), and logic (`/tests`) for high scalability.

### Dockerized Environment
Achieving Environment Parity by running hardware-access tests within isolated containers using `--device` mapping.

### Signal Integrity Analysis
Advanced Python-based integrity analyzer that detects pre-data noise and trailing garbage to identify physical layer instabilities.

## Technical Root-Cause Analysis (Signal Integrity)

During the validation of this framework, a systematic analysis of UART reliability was performed across multiple baud rates.

### Results

- **115,200 Baud**: Achieved **100% stability (PASS)**.
- **460,800+ Baud**: The framework successfully identified **Signal Degradation**.

### Finding

Failures at higher speeds were root-caused to physical constraints of the Raspberry Pi mini-UART and cable interference, rather than software defects.

## How to Run

### Native Execution

```bash
pytest tests/
```

### Docker Execution

```bash
docker build -t hil-tester .
docker run --device=/dev/ttyS0 hil-tester
```