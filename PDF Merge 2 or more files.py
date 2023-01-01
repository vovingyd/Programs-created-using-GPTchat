import os
import sys
from PyPDF2 import PdfReader, PdfMerger

# Get the list of PDF files in the current directory
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]

# Print the list of PDF files and prompt the user to select which ones to merge
for i, pdf_file in enumerate(pdf_files):
    print(f'[{i}] {pdf_file}')
print('Enter the indices of the PDF files to merge, separated by spaces:')
selected_indices = list(map(int, input().split()))

# Get the selected PDF files
selected_pdfs = [pdf_files[i] for i in selected_indices]

# Create a PDF merger object
pdf_merger = PdfMerger()

# Add each selected PDF file to the merger
for pdf in selected_pdfs:
    pdf_merger.append(pdf)

# Merge the PDFs
pdf_merger.write('merged.pdf')

print('PDFs merged successfully!')
