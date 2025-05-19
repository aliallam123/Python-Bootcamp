from PIL import Image

# Open image and get basic info
img = Image.open("sample.jpg")

print("Format:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)
