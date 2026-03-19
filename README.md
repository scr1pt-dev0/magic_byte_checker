# Magic Byte Checker 🔍

A simple Python tool that detects hidden executable files by analyzing their magic bytes - completely ignoring file extensions.

## 🎯 What it does

Every Windows executable (`.exe`, `.dll`) starts with the magic bytes `MZ`. This tool reads the first 2 bytes of any file and checks if they match `MZ` - revealing disguised executables regardless of their filename.

## 🚀 Features

- ✅ Detects EXE files even with fake extensions (e.g., `image.jpg` that's actually an EXE)
- ✅ Catches the "Double Extension" trick (e.g., `document.pdf.exe`)
- ✅ Fast - only reads the first 2 bytes of each file
- ✅ Safe - never modifies or executes files
- ✅ Clear warnings with ASCII art for suspicious files

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/magic_byte_checker.git
cd magic_byte_checker


# No dependencies needed! Just Python 3
