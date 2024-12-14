import re
import string
from text_extraction import get_extracted_text  # text_extraction modülünden fonksiyon çekiliyor


def tokenize_text(text):
    """
    Tokenizes text without depending on NLTK's word_tokenize or sent_tokenize.
    Uses regex and string punctuation for tokenization.
    """
    # Split text on whitespace and remove punctuation
    tokens = re.findall(r"\b\w+(?:['-]\w+)*\b", text)
    return tokens


def extract_entities(text):
    """
    Processes text to extract vendor name (as a proper noun phrase),
    date, and monetary amounts from an invoice.

    Instead of using NLTK's pos_tag (to avoid the missing NLTK averaged perceptron model issue),
    this function uses capitalization heuristics to identify proper nouns.
    """
    # Tokenize text
    tokens = tokenize_text(text)

    # Identify proper nouns based on capitalization
    vendor_names = []
    current_name = []

    for word in tokens:
        if word[0].isupper():  # Proper nouns are usually capitalized
            current_name.append(word)
        elif current_name:
            vendor_names.append(" ".join(current_name))
            current_name = []
    # Add last name if any left
    if current_name:
        vendor_names.append(" ".join(current_name))

    # Regex for dates (example: 12/12/2024)
    date_pattern = r"\d{1,2}/\d{1,2}/\d{4}"
    invoice_dates = re.findall(date_pattern, text)

    # Regex for monetary amounts (example: $250.00)
    money_pattern = r"\$\d+(?:\.\d{2})?"
    amounts = re.findall(money_pattern, text)

    # Return extracted entities
    return {
        "vendor_name": vendor_names,
        "invoice_date": invoice_dates,
        "amount": amounts,
    }


# Test the functionality with imported text from `text_extraction`
if __name__ == "__main__":
    # `get_extracted_text` fonksiyonundan OCR sonucu alınıyor
    ocr_text = get_extracted_text()  # text_extraction modülündeki fonksiyon çağırılıyor

    # OCR'den alınan metni işleyerek gerekli bilgileri çıkar
    entities = extract_entities(ocr_text)

    print("Extracted Entities:")
    print(entities)
