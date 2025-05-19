from PIL import Image

# Open an image
img = Image.open("sample.jpg")

# Show image
img.show()

# Resize image
resized = img.resize((200, 200))
resized.save("resized_sample.jpg")

# Convert to greyscale
grey = img.convert("L")
grey.save("grey_sample.jpg")
