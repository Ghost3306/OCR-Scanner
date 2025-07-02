# OCR-Scanner

OCR-Scanner is a Django web application that allows users to upload image files (e.g., only `.jpg`) and extracts text from them using Optical Character Recognition (OCR) powered by **Tesseract OCR** and **OpenCV**. The extracted text is saved as `.txt` files and stored alongside the original uploaded images.

---

## 🚀 Features

- 📷 Upload image files (JPEG, PNG)
- 🧾 Extract text using Tesseract OCR
- 💾 Save extracted text as `.txt` files
- 🗂️ Store uploaded image and `.txt` file in database (with UUID)
- 🔗 Generate downloadable URLs for `.txt` files

---

## 🛠️ Technologies Used

- Python 3.x
- Django 5.x
- SQLite3 (default)
- OpenCV
- Tesseract OCR


