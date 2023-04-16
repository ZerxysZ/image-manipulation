import os
from PIL import Image

# Create the required directories
if not os.path.exists("images"):
    os.mkdir("images")
if not os.path.exists("png"):
    os.mkdir("png")
if not os.path.exists("thumbnails"):
    os.mkdir("thumbnails")
if not os.path.exists("rotation"):
    os.mkdir("rotation")
if not os.path.exists("black_white"):
    os.mkdir("black_white")
if not os.path.exists("blurred"):
    os.mkdir("blurred")
if not os.path.exists("other_changes"):
    os.mkdir("other_changes")

# Save 10 different JPEG images in the "images" folder
for i in range(10):
    img = Image.new("RGB", (100, 100), (255, 0, 0))
    img.save(f"images/img{i+1}.jpeg")

# Define a function to display the menu and prompt for user input
def menu():
    print("Select an option:")
    print("a. Open an image")
    print("b. Convert JPEG images to PNG and move them to a 'png' folder")
    print("c. View all JPEG and PNG images in their directories")
    print("d. Create thumbnails of selected size and save them to a corresponding folder")
    print("e. Rotate an image to a given length and save it in a 'rotation' folder")
    print("f. Turn an image into black and white and save it in a 'black_white' folder")
    print("g. Blur an image with a user-input value and save it in a 'blurred' folder")
    print("h. Change one other feature of the picture using Pillow library and save it in a corresponding folder")
    print("i. Open all edited images and view them")
    print("j. Exit")

    choice = input("Enter your choice: ")
    return choice.lower()

# Define a function to open an image and display it
def open_image():
    filename = input("Enter the filename of the image (include the extension): ")
    path = f"images/{filename}"
    if os.path.exists(path):
        img = Image.open(path)
        img.show()
    else:
        print("Image not found")

# Define a function to convert JPEG images to PNG and move them to the "png" folder
def convert_to_png():
    for filename in os.listdir("images"):
        if filename.endswith(".jpeg"):
            img_path = os.path.join("images", filename)
            img = Image.open(img_path)
            png_path = os.path.join("png", os.path.splitext(filename)[0] + ".png")
            img.save(png_path)
            os.remove(img_path)

# Define a function to view all JPEG and PNG images in their directories
def view_images():
    print("JPEG images:")
    for filename in os.listdir("images"):
        if filename.endswith(".jpeg"):
            print(filename)
    print("\nPNG images:")
    for filename in os.listdir("png"):
        if filename.endswith(".png"):
            print(filename)

# Define a function to create thumbnails of selected size and save them to a corresponding folder
def create_thumbnail():
    size = int(input("Enter the thumbnail size (in pixels): "))
    for filename in os.listdir("images"):
        if filename.endswith(".jpeg"):
            img_path = os.path.join("images", filename)
            img = Image.open(img_path)
            thumbnail_path = os.path.join("thumbnails", os.path.splitext(filename)[0] + f"_{size}x{size}.jpeg")
            img.thumbnail((size, size))
            img.save(thumbnail_path)

# Define a function to rotate an image to a given length and save it
def rotate_image():
    filename = input("Enter the filename of the image you want to rotate (include the extension): ")
    path = f"images/{filename}"
    if os.path.exists(path):
        img = Image.open(path)
        degrees = int(input("Enter the number of degrees to rotate the image: "))
        rotated_img = img.rotate(degrees)
        save_path = f"rotation/rotated_{filename}"
        rotated_img.save(save_path)
        print(f"Image saved as {save_path}")
    else:
        print("Image not found")

# Define a function to turn an image into black and white and save it
def black_and_white():
    filename = input("Enter the filename of the image you want to convert to black and white (include the extension): ")
    path = f"images/{filename}"
    if os.path.exists(path):
        img = Image.open(path)
        black_white_img = img.convert("L")
        save_path = f"black_white/black_white_{filename}"
        black_white_img.save(save_path)
        print(f"Image saved as {save_path}")
    else:
        print("Image not found")

# Define a function to blur an image with a user-input value and save it
def blur_image():
    filename = input("Enter the filename of the image you want to blur (include the extension): ")
    path = f"images/{filename}"
    if os.path.exists(path):
        img = Image.open(path)
        blur_amount = int(input("Enter the blur amount (in pixels): "))
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius=blur_amount))
        save_path = f"blurred/blurred_{filename}"
        blurred_img.save(save_path)
        print(f"Image saved as {save_path}")
    else:
        print("Image not found")

# Define a function to change one other feature of the picture using Pillow library and save it
def other_changes():
    filename = input("Enter the filename of the image you want to modify (include the extension): ")
    path = f"images/{filename}"
    if os.path.exists(path):
        img = Image.open(path)
        # Add your changes to the image here
        # For example:
        # img = img.filter(ImageFilter.SHARPEN)
        # img = img.transpose(Image.TRANSPOSE)
        save_path = f"other_changes/modified_{filename}"
        img.save(save_path)
        print(f"Image saved as {save_path}")
    else:
        print("Image not found")

# Define a function to open all edited images and view them
def view_edited_images():
    for foldername in ["png", "thumbnails", "rotation", "black_white", "blurred", "other_changes"]:
        print(f"\n{foldername.capitalize()}:")
        for filename in os.listdir(foldername):
            print(filename)
            img = Image.open(os.path.join(foldername, filename))
            img.show()

# Main program loop
while True:
    choice = menu()
    if choice == "a":
        open_image()
    elif choice == "b":
        convert_to_png()
    elif choice == "c":
        view_images()
    elif choice == "d":
        create_thumbnail()
    elif choice == "e":
        rotate_image()
    elif choice == "f":
        black_and_white()
    elif choice == "g":
        blur_image()
    elif choice == "h":
        other_changes()
    elif choice == "i":
        view_edited_images()
    elif choice == "j":
        break
    else:
        print("Invalid choice. Please try again.")
