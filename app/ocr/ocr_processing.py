import os
from text_extraction import extract_text_from_image, extract_entities

def process_uploaded_images():
    upload_folder = os.path.join(os.getcwd(), 'uploads')
    for filename in os.listdir(upload_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_path = os.path.join(upload_folder, filename)
            text = extract_text_from_image(image_path)
            entities = extract_entities(text)
            print(f"Processed {filename}:")
            print(f"Vendor Name: {entities['vendor_name']}")
            print(f"Invoice Date: {entities['invoice_date']}")
            print(f"Amount: {entities['amount']}")