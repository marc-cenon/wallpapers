from PIL import Image
import os

def convert_png_to_jpg(input_folder, output_folder):
    # create output folder if it does not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            # Open the PNG image
            png_image = Image.open(os.path.join(input_folder, filename))

            # Generate the output filename
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            
            # Save the image as JPG
            output_path = os.path.join(output_folder, output_filename)
            png_image.save(output_path, "JPEG")
            print(f"Converted {filename} to {output_filename}")

# Provide the input and output folder paths
input_folder = "."
output_folder = "."

# Convert PNG to JPG
convert_png_to_jpg(input_folder, output_folder)
