import PyPDF2

def merge_pdfs(pdf_files, output_filename):
    """Merge a list of PDF files into a single PDF."""
    merger = PyPDF2.PdfMerger()

    try:
        for filename in pdf_files:
            with open(filename, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                merger.append(pdf_reader)

        merger.write(output_filename)
        print(f"File merged successfully into {output_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        merger.close()


def get_pdf_files_from_user():
    """Prompt the user to enter PDF file paths separated by commas."""
    raw_input_value = input("Enter PDF file paths separated by commas: ").strip()
    pdf_files = [pdf.strip() for pdf in raw_input_value.split(",") if pdf.strip()]
    return pdf_files


def main():
    pdf_files = get_pdf_files_from_user()

    if not pdf_files:
        print("No PDF files were provided.")
        return

    output_file = input("Enter output PDF filename [merged.pdf]: ").strip() or "merged.pdf"
    merge_pdfs(pdf_files, output_file)


if __name__ == "__main__":
    main()
