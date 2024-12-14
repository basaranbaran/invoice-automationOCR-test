import cv2
import numpy as np
import os
import logging

def preprocess_image(image_path):
    # Check if the file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file '{image_path}' does not exist.")

    logging.info(f"Loading image from {image_path}")
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if image is None:
        raise ValueError(
            f"The file '{image_path}' could not be read as an image. Please check if the file is a valid image format.")

    logging.info("Converting image to grayscale")
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    alpha = 0.90  # Kontrast değeri (1.0 değişiklik yapmaz)
    beta = 0.8  # Parlaklık değeri

    logging.info("Adjusting image contrast and brightness")
    adjusted_image = cv2.convertScaleAbs(gray_image, alpha=alpha, beta=beta)

    logging.info("Enhancing image contrast using CLAHE")
    # CLAHE ile kontrast artırımı (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(adjusted_image)

    logging.info("Denoising the image")
    denoised_image = cv2.fastNlMeansDenoising(enhanced_image, None, h=10, templateWindowSize=7, searchWindowSize=21)

    return denoised_image


# Test the function
if __name__ == "__main__":
    # Determine the base directory (project root)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

    # Construct full paths for input and output files
    input_path = os.path.join(base_dir, "data/kaggle_data/archive/X00016469619.jpg")
    output_path = os.path.join(base_dir, "data/processed/invoice2_processed4.jpg")

    try:
        logging.info(f"Processing image at {input_path}")
        processed_image = preprocess_image(input_path)

        # Ensure the output directory exists before saving the processed image to it
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        logging.info(f"Saving processed image to {output_path}")
        # Save the processed image
        cv2.imwrite(output_path, processed_image)
        logging.info(f"Processed image saved at '{output_path}'.")

        # Show the processed image in a window
        cv2.imshow("Processed Image", processed_image)
        cv2.waitKey(5000)  # Display the window for 5000 milliseconds (5 seconds)
        cv2.destroyAllWindows()

    except Exception as e:
        logging.error(f"An error occurred: {e}")