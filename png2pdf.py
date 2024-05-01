# Author: Fibogacci, 20240501
# github.com/Fibogacci
# Licence: MIT
# Script for merging PNG files into PDF
                                                import argparse                                                             from reportlab.pdfgen import canvas                                         from PIL import Image                                                       
import os
import argparse
from reportlab.pdfgen import canvas
from PIL import Image

def main():                                                                     parser = argparse.ArgumentParser(description="Convert PNG images in a folder to a PDF file, with each page sized to match the image.")
    parser.add_argument("-p", "--folder_path", help="Path to the folder containing PNG images.", required=True)                                             parser.add_argument("-o", "--output", help="Name of the output PDF file.", default="output.pdf")

    args = parser.parse_args()

    folder_path = args.folder_path
    output_pdf_path = os.path.join(folder_path, args.output)

    # Initialize the canvas but without setting pagesize yet
    c = canvas.Canvas(output_pdf_path)

    # Get all PNG files from the folder
    images = [os.path.join(folder_path, img) for img in os.listdir(folder_path) if img.endswith(".png")]                                                    images.sort()  # Sort files alphabetically

    for image_path in images:                                                       pil_image = Image.open(image_path)
        # Ensure image is in RGB mode (necessary for color images)
        if pil_image.mode != "RGB":
            pil_image = pil_image.convert("RGB")

        img_width, img_height = pil_image.size
        # Set the pagesize to the image size for each new page
        c.setPageSize((img_width, img_height))

        # Draw the image on the canvas                                              c.drawInlineImage(pil_image, x=0, y=0, width=img_width, height=img_height)
                                                                                    # Add a new page for the next image
        c.showPage()

    # Save the PDF
    c.save()

    print(f"Created PDF: {output_pdf_path}")

if __name__ == "__main__":
    main()
