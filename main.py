# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter
import sys
sys.stdout.reconfigure(encoding='utf-8')
import time
import os

def welcome_messages():
    print("Greetings Mr. Rai! Welcome to my image manipulation assignment (with some starcraft/overwatch images 😇) Lord Kerrigan has granted you the power to manipulate the following jpeg pictures:")
    options = ['power to resize 🦿', 'ability to rotate 😵‍💫', 'potential of converting to png and saving them 😮‍💨', 'you can blur 😶‍🌫️', 'convert to black & white 🥷', 'you can pick which one to open 🧗🏽', 'you can view all jpeg and png 👀', 'you can change the colour to blue 🧢', 'you can open all the edited images 💍👑', 'and finally, you have the ability to manipulate all these changes to an image 🤝']
    for option in options:
        print(option)
        time.sleep(0.7)
    
def image_show():
    print('Choose any of the coveted images: ')
    options = ['arcturus', 'fenix', 'genji', 'hanzo', 'kerrigan', 'mercy', 'ow', 'raynor', 'starcraft', 'zeratul']
    for option in options:
        print(option)
        time.sleep(0.7)
    
    while True:
        user_input = input('Enter the name of the image you want to open/edit or press "q" to quit: ').lower()
        
        if user_input == 'arcturus':
            image = Image.open('arcturus.jpeg')
            image.show()
        
        elif user_input == 'fenix':
            image = Image.open('fenix.jpeg')
            image.show()
            
        elif user_input == 'genji':
            image = Image.open('genji.jpeg')
            image.show()
        
        elif user_input == 'hanzo':
            image = Image.open('hanzo.jpeg')
            image.show()
            
        elif user_input == 'kerrigan':
            image = Image.open('kerrigan.jpeg')
            image.show()
        
        elif user_input == 'mercy':
            image = Image.open('mercy.jpeg')
            image.show()
            
        elif user_input == 'ow':
            image = Image.open('ow.jpeg')
            image.show()
        
        elif user_input == 'raynor':
            image = Image.open('raynor.jpeg')
            image.show()
            break 
        
        elif user_input == 'starcraft':
            image = Image.open('starcraft.jpeg')
            image.show()
        
        elif user_input == 'zeratul':
            image = Image.open('zeratul.jpeg')
            image.show()
        
        elif user_input == 'q':
            break
        
        else:
            print('Invalid input. Please Re-Enter.')
    
def image_png():
    print('You have the power to change the JPEG images to a PNG file')
    user_input = input('Are you interested in converting them? Enter y/n: ').lower()
    if user_input == 'n':
        print('Thanks for nothing!')
        return
    elif user_input == 'y':
        for i in os.listdir('.'):
            if i.endswith('.jpeg'):
                a = Image.open(i)
                file_name, file_ext = os.path.splitext(i)
                a.save('pngfolder/{}.png'.format(file_name))
        print('Images converted successfully!')
    else:
        print('An error has occurred. Please enter y/n.')

def image_resize():
    print('Are you interested in resizing images?')
    while True:
        user_input = input('Enter y/n: ').lower()
        if user_input == 'n':
            print('No problem!')
            break
        elif user_input == 'y':
            print('Great!')
            while True:
                image_name = input('Enter the name of the image to resize (or q to exit): ')
                if image_name == 'q':
                    break
                try:
                    image = Image.open(image_name)
                except FileNotFoundError:
                    print('File not found. Please try again.')
                    continue
                
                while True:
                    width = input('Enter the desired width (or q to exit): ')
                    if width == 'q':
                        break
                    try:
                        width = int(width)
                        break
                    except ValueError:
                        print('Invalid input. Please enter a valid integer value.')
                
                if width == 'q':
                    break
                
                while True:
                    height = input('Enter the desired height (or q to exit): ')
                    if height == 'q':
                        break
                    try:
                        height = int(height)
                        break
                    except ValueError:
                        print('Invalid input. Please enter a valid integer value.')
                
                if height == 'q':
                    break
                
                resized_image = image.resize((width, height))
                file_name, file_ext = os.path.splitext(image_name)
                resized_image.save('resized/{}{}{}'.format(file_name, '_', file_ext))
                print('Image saved in "resized" folder!')
        else:
            print('Invalid input. Please try again.')

def image_rotate():
    print('Do you want to rotate the image?')
    while True:
        user_input = input('Enter y/n: ').lower()
        if user_input == 'n':
            print('No problem!')
            break
        elif user_input == 'y':
            print('Great!')
            while True:
                image_name = input('Enter the name of the image to rotate (or q to exit): ')
                if image_name == 'q':
                    break
                try:
                    image = Image.open(image_name)
                except FileNotFoundError:
                    print('File not found. Please try again.')
                    continue
                
                while True:
                    degree = input('Enter the degree to rotate (or q to exit): ')
                    if degree == 'q':
                        break
                    try:
                        degree = int(degree)
                        break
                    except ValueError:
                        print('Invalid input. Please enter a valid integer value.')
                
                if degree == 'q':
                    break
                
                rotated_image = image.rotate(degree)
                file_name, file_ext = os.path.splitext(image_name)
                rotated_image.save('rotated/{}{}{}'.format(file_name, '_', file_ext))
                print('Image saved in "rotated" folder!')
        else:
            print('Invalid input. Please try again.')

def black_and_white(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding
    thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    
    return thresholded

def image_blur():
    print('Are you interested in blurring images?')
    while True:
        user_input = input('Enter y/n: ').lower()
        if user_input == 'n':
            print('No problem!')
            break
        elif user_input == 'y':
            print('Great!')
            while True:
                image_name = input('Enter the name of the image to blur (or q to exit): ')
                if image_name == 'q':
                    break
                try:
                    image = Image.open(image_name)
                except FileNotFoundError:
                    print('File not found. Please try again.')
                    continue
                
                blurred_image = image.filter(ImageFilter.BLUR)
                file_name, file_ext = os.path.splitext(image_name)
                blurred_image.save('blurred/{}{}{}'.format(file_name, '_', file_ext))
                print('Image saved in "blurred" folder!')
        else:
            print('Invalid input. Please try again.')

def image_diff_color():
    while True:
        user_input = input('Do you want to alter Fenixes colour? Please enter y/n: ')
        user_input = user_input.lower()
        if user_input == 'y':
            red_image = Image.open('fenix.jpeg')
            red_image = red_image.convert('RGB')
            width, height = red_image.size
            for x in range(width):
                for y in range(height):
                    r, g, b = red_image.getpixel((x, y))
                    red_image.putpixel((x, y), (r, 0, 0))
            red_image.save('fenix_red.jpeg')
            red_image.show()
            break
        elif user_input == 'n':
            break
        else:
            print('Invalid input. Please enter y or n.')

folder2 = 'pngfolder'
def view_png_DUPE(filename):
    return filename.lower().endswith(('.jpeg', '.png'))

def view_png_images(folder):
    for filename in os.listdir(folder):
        if view_png_DUPE(filename):
            filepath = os.path.join(folder, filename)
            image = Image.open(filepath)
            image.show()

def view_bnw_images():
    folderbnw = 'converted_images'
    for filename in os.listdir(folderbnw):
        filepath = os.path.join(folderbnw, filename)
        try:
            with Image.open(filepath) as img:
                if img.mode == 'L':
                    img.show()
        except IOError:
            continue

def view_rotated_images():
    messedup_folder = 'rotated_images'
    for filename in os.listdir(messedup_folder):
        file = os.path.join(messedup_folder, filename)
        try:
            with Image.open(file) as img:
                if hasattr(img, '_getexif'):
                    exif = img._getexif()
                    if exif:
                        looks = exif.get(0x0112)
                        if looks in [3, 6, 8]:
                            if looks == 3:
                                angle = 180
                            elif looks == 6:
                                angle = 270
                            elif looks == 8:
                                angle = 90
                            img = img.rotate(angle, expand=True)
                img.show()
        except IOError:
            continue

def view_resized_200():
    folder_resize = 'size200'
    for filename in os.listdir(folder_resize):
        file = os.path.join(folder_resize, filename)
        try:
            with Image.open(file) as img:
                if img.size != (200, 200):
                    img.show()
        except IOError:
            continue

def view_resized_400():
    folder_resize = 'size400'
    for filename in os.listdir(folder_resize):
        file = os.path.join(folder_resize, filename)
        try:
            with Image.open(file) as img:
                if img.size != (400, 400):
                    img.show()
        except IOError:
            continue

def view_resized_600():
    folder_resize = 'size600'
    for filename in os.listdir(folder_resize):
        file = os.path.join(folder_resize, filename)
        try:
            with Image.open(file) as img:
                if img.size != (600, 600):
                    img.show()
        except IOError as e:
            print(f"Error opening {file}: {e}")

def view_jpeg_images():
    folder_path = 'jpegfolder'

    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:
                img.show()


def view_all_edits_MAIN():
    while True:
        user = input('Are you interested in viewing all PNG files? If so, please enter y/n: ')
        user = user.lower()
        if user == 'y':
            view_png_images(folder2)
            break

        elif user == 'n':
            break

        else:
            print('Invalid input. Please try again.')

    while True:
        user = input('Are you interested in viewing all black and white files? Please enter y/n: ')
        user = user.lower()
        if user == 'y':
            view_bnw_images()
            break

        elif user == 'n':
            break

        else:
            print('Invalid input. Please try again.')

    while True:
        user = input('Interested in viewing all rotated files? Please enter y/n: ')
        user = user.lower()
        if user == 'y':
            view_rotated_images()
            break

        elif user == 'n':
            break

        else:
            print('Invalid input. Please try again.')

    while True:
        user = input('Would you like to see it resized to 200x200? Please enter y/n: ')
        user = user.lower()
        if user == 'y':
            view_resized_200()
            break

        elif user == 'n':
            break

        else:
            print('Invalid input. Please try again.')

    while True:
        user = input('Would you like to see it resized to 400x400? Please enter y/n: ')
        user = user.lower()
        if user == 'y':
            view_resized_400()
            break

        elif user == 'n':
            break

        else:
            print('Invalid input. Please try again.')

    while True:
        user = input('Would you like to see it resized to 600x600? Please enter y/n: ')
        user = user.lower()
        if user == 'y':
            view_resized_600()
            break

        elif user == 'n':
            break

        else:
            print('Invalid input. Please try again.')

    while True:
        user = input('Interested in viewing Arcturus\'s blurred file? Please enter y/n: ')
        user = user.lower()
        if user == 'y':
            image_blur()
            break

        elif user == 'n':
            break

        else:
            print('Invalid input. Please try again.')

    while True:
        user = input('Would you like to view Fenix\'s coloured file? Please enter y/n: ')
        user = user.lower()
        if user == 'y':
            image_diff_color()
            break

        elif user == 'n':
            break

        else:
            print('Invalid input. Please try again.')

    while True:
        user = input('Interested in viewing all JPEG files? Please enter y/n: ')
        user = user.lower()
        if user == 'y':
            view_jpeg_images()
            break

        elif user == 'n':
            break

        else:
            print('Invalid input. Please try again.')

    return

welcome_messages()
image_show()
image_png()
image_resize()
image_rotation()
image_bnw()
image_blur()
image_diff_color()
view_jpeg_images()
view_all_edits_MAIN()
