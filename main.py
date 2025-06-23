from random import sample
import PyPDF2

def merge_pdfs(pdf_files, output_filename):
    """
    Merges a list of PDF files into a single PDF.

    Args:
        pdf_files (list): A list of PDF file paths to be merged.
        output_filename (str): The filename of the output merged PDF.
    """
    merger = PyPDF2.PdfMerger()
    
    try:
        for filename in pdf_files:
            with open(filename, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                merger.append(pdf_reader)
        
        merger.write(output_filename)
        print(f"File merged successfully into {output_filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        merger.close()



pdf_files = ["1.pdf", "php.pdf", "php1.pdf"]
output_file = "merged.pdf"
merge_pdfs(pdf_files, output_file)
