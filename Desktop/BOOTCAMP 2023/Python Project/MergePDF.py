
import tkinter as tk
from tkinter import filedialog
from pypdf import PdfWriter

# Create a tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Ask the user to select PDF files using a file dialog
pdf_files = filedialog.askopenfilenames(
    title="Select PDF Files",
    filetypes=[("PDF Files", "*.pdf")],
)

if not pdf_files:
    print("No PDF files selected. Exiting.")
else:
    # Create a PdfFileMerger instance and merge the selected PDF files
    merger = PdfWriter()

    for pdf in pdf_files:
        merger.append(pdf)

    merged_filename = "merged-pdf.pdf"
    merger.write(merged_filename)
    merger.close()

    print(f"Merged PDF saved as '{merged_filename}'")

# Close the tkinter root window (optional)
root.quit()
