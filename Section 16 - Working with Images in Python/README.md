# 🖼️ Working with Images in Python

### Library: PIL (Pillow)
- `Pillow` is the friendly fork of PIL – used for image processing in Python.
- Install it using `pip install Pillow`.

---

### 🔧 Basic Operations
- **Open an image**: `Image.open("file.jpg")`
- **Show image**: `img.show()`
- **Resize**: `img.resize((width, height))`
- **Convert to greyscale**: `img.convert("L")`
- **Save**: `img.save("new_file.jpg")`

---

### ℹ️ Image Info
- `img.format` → JPEG, PNG, etc.
- `img.size` → (width, height)
- `img.mode` → "RGB", "L" (greyscale), etc.

---

### 🧠 Quick Tips
- Always save modified images with a new filename to avoid overwriting the original.
- Greyscale = easier for some types of image processing (e.g. filtering).
- Pillow also supports cropping, rotating, drawing, and more — explore it as you go!
