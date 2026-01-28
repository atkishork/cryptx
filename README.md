# CRYPTX 🔐

**CRYPTX** is a fast, CTF-focused encoder/decoder CLI tool for Linux.  
It supports base encodings, classical ciphers, numeric conversions, URL encoding, XOR operations, and is fully scriptable with piping and file I/O.

---

## Features

- Base encodings: **base32, base45, base58, base62, base64, base85**
- Classical cipher: **ROT / Caesar (-r)**
- Numeric & binary conversions: **hex, binary, decimal, octal**
- XOR cipher: **(-k key)**
- URL encode/decode
- Native man page (`cryptx --man`)
- Fully offline and scriptable

---

## Table of Contents

1. [Installation](#installation)  
2. [Usage](#usage)  
3. [Pipe & File Support](#pipe--file-support)  
4. [Manual Page](#manual-page)  
5. [Examples](#examples)  
6. [Uninstallation](#uninstallation)  
7. [Author & License](#author--license)  

---

## Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/atkishork/cryptx.git
cd cryptx
```
### 2️⃣ Using pipx (recommended)
```bash
pipx install .
```
### 3️⃣ Check installation
```bash
which cryptx
cryptx --man  (manual page)
cryptx -h  (help page)
```
### 4️⃣ Examples:--
```bash
# Base64 encode
cryptx -e base64 "hello world"

# Base64 decode
cryptx -d base64 "aGVsbG8gd29ybGQ="

# ROT cipher encode
cryptx -e rot "hello" -r 13

# ROT cipher decode
cryptx -d rot "uryyb" -r 13

# XOR encode/decode
cryptx -e xor "secret" -k 42
cryptx -d xor "someoutput" -k 42

# Hex encoding/decoding
cryptx -e hex "hello"
cryptx -d hex "68656c6c6f"
```
### 5️⃣ Uninstall
```bash
pipx uninstall cryptx
```

###Author & License
Author: Kishor Kumar
GitHub: https://github.com/atkishork
License: MIT License
