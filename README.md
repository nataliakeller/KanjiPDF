# KanjiPDF
This Python script is designed to generate images containing individual kanji characters from a CSV file.


# Kanji Image Generator

This Python script is designed to generate images containing individual kanji characters from a CSV file. The kanjis are rendered on a predefined template, and each kanji is placed in specific locations on the image. The script processes kanji strings by splitting them into individual kanji characters, ensuring that only kanji are included (ignoring hiragana, katakana, and other characters). The result is a series of images where each kanji is centered and ready for use in flashcards or other study materials.

## Features:
- **Kanji Separation**: Automatically splits kanji strings into individual kanji characters.
- **Unicode Filtering**: Ignores hiragana, katakana, and non-kanji characters.
- **Template-Based Rendering**: Uses a predefined template where kanjis are placed at specific coordinates.
- **Font Customization**: Uses a Japanese font to render kanji characters, with adjustable font size.
- **Pagination**: Automatically generates multiple pages if there are more kanjis than can fit on a single page.

## Requirements:
- Python 3.x
- **Pillow (PIL)** - For image manipulation.
- **Pandas** - For reading and processing CSV files.
- **Font**: A Japanese font (e.g., BIZ-UDMinchoM) for rendering kanji characters.

## How to Use:
1. Prepare a CSV file (`kanjis.csv`) with a column containing kanji strings. Example:
    ```csv
    Sort Field
    必要
    告白
    経験
    場合
    欠伸
    想い
    ```

2. Ensure the template image (`template.jpg`) is in the same directory as the script, or provide the correct path.
3. Customize the font and font size as necessary (default font size is 92).
4. Run the script, and the kanji images will be saved as `Filled_Page_1.jpg`, `Filled_Page_2.jpg`, etc.

## How It Works:
- The script will read the kanji strings from the CSV file and separate them into individual kanji characters, ignoring hiragana and katakana.
- Each kanji will be placed in predefined positions on the template. If there are more kanjis than can fit on a page, the script will automatically create additional pages.
- The kanjis are centered within their respective boxes, and the result is saved as an image for each page.

## Notes:
- The script uses the `textbbox` method to calculate the proper dimensions for centering each kanji.
- The positions on the template can be adjusted in the `kanji_positions` list.
