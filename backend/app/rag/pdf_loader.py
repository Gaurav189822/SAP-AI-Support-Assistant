from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):

    print("\nExtracting PDF text...")

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:

            text += extracted + "\n"

    print("PDF text extraction completed!")

    return text