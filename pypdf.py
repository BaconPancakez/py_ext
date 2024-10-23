import PyPDF2

# Open the first PDF file and read its content
with open('first.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print('number of pages: ', len(reader.pages))  # Print number of pages

    page = reader.pages[0]  # Get the first page
    page.rotate(angle=90)  # Rotate the first page by 90 degrees

    writer = PyPDF2.PdfWriter()
    writer.add_page(page)  # Add the rotated page

    # Write the rotated page to a new PDF
    with open('rotated.pdf', 'wb') as output:
        writer.write(output)

# Merge multiple PDFs into one
merger = PyPDF2.PdfMerger()
file_names = ['first.pdf', 'second.pdf']  # List of files to merge
for file_name in file_names:
    merger.append(file_name)  # Append each file

# Write the merged PDF to a new file
merger.write('combined.pdf')
