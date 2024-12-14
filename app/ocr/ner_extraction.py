import re
from text_extraction import get_extracted_text


def extract_entities(text):
    """Extracts vendor name, date, and amounts using regex and keyword matching."""
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    lines = text.split("\n")

    vendor_name = None
    date = None
    amount = None
    amounts = []

    # Define ignore keywords to exclude irrelevant lines
    ignore_keywords = [
        "total", "invoice", "amount", "balance", "subtotal", "date", "number",
        "tax", "reference", "payment", "charges", "due", "receipt"
    ]

    # Improved Vendor Name Extraction
    keywords = [
        "sdn bhd", "enterprise", "marketing", "restaurants", "restaurant",
        "cafe", "trading", "supplies", "company", "inc", "ltd", "corporation",
        "limited", "solutions", "industries", "services", "group", "holding"
    ]

    vendor_candidates = []

    # Regex to capture potential vendor names
    vendor_pattern = re.compile(r'^[a-zA-Z0-9&\'\-.\s()]+$')

    for line in lines:
        line = line.strip()
        # Match the vendor pattern
        if vendor_pattern.match(line):
            # Exclude lines that are clearly not vendor names
            if not any(keyword in line.lower() for keyword in ignore_keywords):
                vendor_candidates.append(line)

    # Check for keywords (case insensitive) in all lines
    for line in lines:
        if any(keyword in line.lower() for keyword in keywords) or any(keyword in line.upper() for keyword in keywords):
            vendor_name = line.strip()  # Eğer satırda keyword varsa direkt al
            break

    # Eğer hala vendor_name bulunmadıysa alternatif olarak ilk uygun adayı belirle
    if not vendor_name and vendor_candidates:
        # Pick the topmost candidate, prioritizing longer lines
        vendor_name = max(vendor_candidates, key=len)

    # Date extraction
    date_pattern = re.compile(r'(\d{1,2}/\d{1,2}/\d{4})')
    for line in lines:
        date_match = date_pattern.search(line)
        if date_match:
            date = date_match.group()
            break

    # Amount extraction (Search for "Total", "Nett Total", "Amount" and money pattern)
    amount_pattern = re.compile(r'[\$\s]*([\d.,]+)')
    for line in lines:
        if "total" in line.lower() or "nett total" in line.lower() or "amount" in line.lower():
            match = amount_pattern.search(line)
            if match:
                amounts.append(match.group(1))

    if amounts:
        # Last matched amount is usually the most relevant
        amount = amounts[-1]

    return {
        "vendor_name": vendor_name,
        "invoice_date": date,
        "amount": amount,
    }


def refine_extracted_data(extracted_entities):
    """Refines extracted data and formats as required."""
    refined_data = {
        "vendor_name": extracted_entities.get("vendor_name"),
        "invoice_date": extracted_entities.get("invoice_date"),
        "amount": extracted_entities.get("amount")
    }

    return refined_data


if __name__ == "__main__":
    # Step 1: Use OCR to extract text from the image
    ocr_text = get_extracted_text()

    if not ocr_text:
        print("Error: Unable to extract text from the image. Please check your OCR settings or input file.")
    else:
        # Step 2: Extract basic entities from the OCR text
        extracted_entities = extract_entities(ocr_text)

        # Step 3: Refine the extracted entities to match the desired format
        refined_data = refine_extracted_data(extracted_entities)

        # Step 4: Print the results in the desired format
        print("Refined Data:")
        print(f"Vendor Name: {refined_data['vendor_name']}")
        print(f"Invoice Date: {refined_data['invoice_date']}")
        print(f"Amount: {refined_data['amount']}")
