import os
import pytesseract
from PIL import Image


def extract_text_from_image(image_path):
    """
    Extracts text from the provided image path using Tesseract OCR.
    """
    # Ensure the file exists before proceeding
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist. Please check the path.")

    # Load the image
    image = Image.open(image_path)

    # Extract text using OCR
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text


def get_extracted_text():
    """
    Retrieves extracted text using a predefined image. To make this dynamic,
    you can modify the image path and pass it as an argument wherever needed.
    """
    # Dynamically construct the file path to the image
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    image_path = os.path.join(base_dir, "data", "kaggle_data", "archive", "X00016469612.jpg")

    try:
        # Extract text from the image
        extracted_text = extract_text_from_image(image_path)
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
