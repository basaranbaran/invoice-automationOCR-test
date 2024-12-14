import logging
import os
import pytesseract
from PIL import Image

def extract_text_from_image(image_path, confidence_threshold=60):
    """
    Extracts text from the provided image path using Tesseract OCR.
    Only includes lines with words having confidence scores above the threshold.
    """
    # Ensure the file exists before proceeding
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist. Please check the path.")

    # Load the image
    image = Image.open(image_path)

    # Extract text using OCR with detailed data
    ocr_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    # Filter lines based on confidence score
    extracted_lines = []
    current_line = []
    last_line_num = -1

    for i, word in enumerate(ocr_data['text']):
        if int(ocr_data['conf'][i]) > confidence_threshold:
            line_num = ocr_data['line_num'][i]
            if line_num != last_line_num:
                if current_line:
                    extracted_lines.append(' '.join(current_line).strip())
                current_line = [word]
                last_line_num = line_num
            else:
                current_line.append(word)

    if current_line:
        extracted_lines.append(' '.join(current_line).strip())

    # Remove empty lines
    extracted_lines = [line for line in extracted_lines if line]

    return '\n'.join(extracted_lines)

def get_extracted_text():
    """
    Retrieves extracted text using a predefined image. To make this dynamic,
    you can modify the image path and pass it as an argument wherever needed.
    """
    # Dynamically construct the file path to the image
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    image_path = os.path.join(base_dir, "data", "processed", "invoice2_processed4.jpg")

    try:
        # Extract text from the image
        extracted_text = extract_text_from_image((image_path))
        return extracted_text
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Test the function
if __name__ == "__main__":
    ocr_text = get_extracted_text()

    if ocr_text:
        print("Extracted text:")
        print(ocr_text)
    else:
        print("Failed to extract text from the image.")