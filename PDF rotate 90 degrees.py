import os
import PyPDF2

# Get a list of all PDF files in the current directory
pdf_files = [f for f in os.listdir() if f.endswith('.pdf')]

# Print the list of PDF files and ask the user to select one
print("Select a PDF file to rotate:")
for i, pdf_file in enumerate(pdf_files):
    print(f"{i+1}. {pdf_file}")
selected = int(input())

# Open the selected PDF file in read-binary mode
with open(pdf_files[selected-1], 'rb') as file:
    # Create a PDF object
    pdf = PyPDF2.PdfReader(file)

    # Iterate over each page
    for page in pdf.pages:
        # Rotate the page 90 degrees clockwise
        page.rotate(90)

    # Create a PDF file to write the output
    with open('output.pdf', 'wb') as output:
        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Add the rotated pages to the PDF writer
        for page in pdf.pages:
            pdf_writer.add_page(page)

        # Write the output to the output PDF file
        pdf_writer.write(output)

print("PDF rotated and saved as 'output.pdf'.")
