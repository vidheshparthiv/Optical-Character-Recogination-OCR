# Optical Character Recognition (OCR) 📸 → 📝

Convert text in images into editable, copyable text.

---

## Table of Contents

| Section | Description |
|--------|-------------|
| [About](#about) | What this project does |
| [Features](#features) | Key capabilities |
| [Directory Structure](#directory-structure) | Project layout |
| [Requirements](#requirements) | Dependencies, environment |
| [Installation & Usage](#installation--usage) | How to run it |
| [Examples](#examples) | Sample inputs & outputs |
| [Tips & Best Practices](#tips--best-practices) | Suggestions to improve accuracy |
| [Contributing](#contributing) | How to help |
| [License](#license) | License info |

---

## About

This repository implements a simple OCR (Optical Character Recognition) utility using Python — you feed it an image, and it outputs text found in the image.

It’s handy for scanning documents, extracting text from screenshots, or building further in a pipeline (e.g. translation, summarization).

---

## Features

- Supports image → text conversion  
- Works with common image formats (JPEG, PNG, etc.)  
- Lightweight and easy to extend  
- Minimal dependencies  

---

---

## Requirements

| Package | Version / Notes |
|--------|------------------|
| Python | 3.7+ recommended |
| pytesseract | OCR engine wrapper |
| pillow (PIL) | Image processing |
| opencv-python | Optional — advanced image preprocessing |

You’ll need to have **Tesseract OCR** installed on your system. On Ubuntu:

```bash
sudo apt update
sudo apt install tesseract-ocr

##Installation & Usage

Clone the repo

git clone https://github.com/vidheshparthiv/Optical-Character-Recogination-OCR.git
cd Optical-Character-Recogination-OCR


Install Python dependencies

pip install -r requirements.txt


Run the script

python source.py path/to/your/image.png

