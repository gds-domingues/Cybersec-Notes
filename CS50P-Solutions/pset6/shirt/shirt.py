from PIL import Image, ImageOps
import sys, os

def main():
    # Check the number and validity of command-line arguments
    arguments_check()
    
    # Check file extensions
    extention_check()
    
    # Resize and compose images
    shirt_resize()

def arguments_check():
    # Check the number and validity of command-line arguments
    if len(sys.argv) != 3:
        sys.exit('Usage: python script.py input_image.jpg output_image.jpg shirt.png')
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("Invalid input image path")

def shirt_resize():
    try:
        # Open the shirt and input images
        shirt = Image.open('shirt.png')
        image = Image.open(sys.argv[1])

        # Resize the input image to match the shirt size
        image = ImageOps.fit(image, shirt.size)

        # Paste the shirt onto the input image
        image.paste(shirt, (0, 0), shirt)

        # Save the composed image
        image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit('File not found')

def extention_check():
    # Check file extensions
    input_extension = os.path.splitext(sys.argv[1])[1]
    output_extension = os.path.splitext(sys.argv[2])[1]

    if input_extension != output_extension:
        sys.exit('Files must have the same extension')
        
if __name__ == "__main__":
    main()

"""
This script ensures that the correct number of command-line arguments is provided, 
checks the validity of the file paths, verifies that the input and output files have the same extension, 
and then resizes and composes the images.
"""