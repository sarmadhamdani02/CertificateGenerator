from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# excel_data = pd.read_excel("nameData.xlsx", engine='openpyxl')  # Make sure the file path is correct
# names = excel_data.iloc[:, 6]  # Assuming the 7th column contains the names
names = ["Ahmed Kamal", "Qaseem Sajjad"]  # Assuming the 7th column contains the names

# Folder to save generated certificates
output_folder = "generated_certificates"
os.makedirs(output_folder, exist_ok=True)

# Load certificate template
template_image_path = "certificate.png"  # Replace with your certificate template path
for name in names:
    # Open a fresh copy of the template
    image = Image.open(template_image_path)
    draw = ImageDraw.Draw(image)
    
    # Process name to ensure proper capitalization
    name_text = name.title()

    # Define font and font size
    font_size = 150
    font = ImageFont.truetype("BrittanySignature.ttf", font_size)  # Replace with your font path if needed

    # Get text size and calculate position
    text_bbox = draw.textbbox((0, 0), name_text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    x = (image.width - text_width) / 2
    y = (image.height - text_height) / 2.5  # Adjust Y position as needed

    # Draw name text onto certificate
    draw.text((x, y), name_text, fill="black", font=font)  # Adjust color if needed

    # Save the personalized certificate
    output_path = os.path.join(output_folder, f"{name_text}.png")
    image.save(output_path)

    print(f"Certificate Created for {name_text} ✅")


print("----------------------------------------------")
print("Certificates generated with capitalized names!")
