import unicodedata
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import math

# File paths
template_path = 'template.jpg'
csv_file_path = 'testing.csv'
output_path = 'Filled_Page_{}.jpg'  # Output file name with index for pages

# Load the template and the CSV
template_image = Image.open(template_path)
kanji_data = pd.read_csv(csv_file_path)

# Load the Japanese font
font_path = "C:/Windows/Fonts/BIZ-UDMinchoM.ttc"  # Replace if necessary
font_size = 92  # Increased to better fill the space
font = ImageFont.truetype(font_path, font_size)

# Function to check if the character is a kanji
def is_kanji(char):
    return 'CJK' in unicodedata.name(char)  # Checks if the character belongs to the CJK block (Kanji)

# Function to separate the kanjis and filter only the kanji characters
def separate_kanji(kanji_str):
    return [char for char in kanji_str if is_kanji(char)]

# List of kanjis
kanji_list = kanji_data['Sort Field'].tolist()

# Filter the kanjis and separate the characters, ignoring katakana and hiragana
filtered_kanji_list = []
for kanji_str in kanji_list:
    kanji_chars = separate_kanji(kanji_str)
    filtered_kanji_list.extend(kanji_chars)  # Add the filtered kanjis to the final list

# Define the coordinates for the kanji fields on the template
kanji_positions = [
    (100, 135), (100, 400), (100, 650), (100, 910), (100, 1180), (100, 1430)
]

# Maximum number of kanjis per image
kanjis_per_page = len(kanji_positions)

# Calculate the number of pages needed
num_pages = math.ceil(len(filtered_kanji_list) / kanjis_per_page)

# Create an image for each page
for page in range(num_pages):
    # Load a copy of the template for each page
    template_copy = template_image.copy()
    draw = ImageDraw.Draw(template_copy)
    
    # Determine the range of kanjis for this page
    start_idx = page * kanjis_per_page
    end_idx = start_idx + kanjis_per_page
    kanjis_on_page = filtered_kanji_list[start_idx:end_idx]
    
    # Draw the kanjis on the template
    for idx, kanji in enumerate(kanjis_on_page):
        x, y = kanji_positions[idx]
        
        # Calculate the centered position using textbbox to measure the kanji size
        bbox = draw.textbbox((0, 0), kanji, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        centered_x = x - text_width // 2 + 50  # Adjustment to center in the box
        centered_y = y - text_height // 2 + 50
        
        draw.text((centered_x, centered_y), kanji, fill="black", font=font)
    
    # Save the result for this page
    template_copy.save(output_path.format(page + 1))
    print(f"Image saved as {output_path.format(page + 1)}")
