import PyPDF2
import os

def merge_pdfs(directory, output_path):
    pdf_merger = PyPDF2.PdfMerger()
    
    # Get list of all PDF files in the directory
    pdf_list = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    pdf_list.sort()  # Optional: Sort the files alphabetically
    
    for pdf in pdf_list:
        pdf_path = os.path.join(directory, pdf)
        pdf_merger.append(pdf_path)
    
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":
    # Directory containing PDF files
    directory = os.getcwd()  # Get current working directory
    # Output path for the merged PDF
    output = 'merged.pdf'
    
    merge_pdfs(directory, output)
    print(f"Merged PDF saved as {output}")
