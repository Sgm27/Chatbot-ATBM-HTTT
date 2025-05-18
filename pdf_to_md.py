import fitz  # PyMuPDF
import re
import os

def convert_pdf_to_markdown(pdf_path, output_path):
    """Convert PDF to Markdown format and save to the output path."""
    print(f"Converting {pdf_path} to {output_path}...")
    
    # Open the PDF
    doc = fitz.open(pdf_path)
    markdown_content = []
    
    # Process each page
    for page_num, page in enumerate(doc):
        # Extract text from the page
        text = page.get_text()
        
        # Skip empty pages
        if not text.strip():
            continue
        
        # Process the text for markdown formatting
        
        # Split text into lines
        lines = text.split('\n')
        processed_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Detect headings (assume larger fonts or specific formatting)
            if len(line) < 100 and line.isupper():  # Simple heuristic for headings
                processed_lines.append(f"# {line}")
            elif len(line) < 80 and line[0].isupper() and line[-1] not in [',', ';']:
                processed_lines.append(f"## {line}")
            else:
                processed_lines.append(line)
        
        # Join processed lines with newlines
        processed_text = '\n\n'.join(processed_lines)
        markdown_content.append(processed_text)
    
    # Combine all pages
    full_markdown = '\n\n---\n\n'.join(markdown_content)
    
    # Write to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_markdown)
    
    print(f"Conversion completed. Markdown saved to {output_path}")

if __name__ == "__main__":
    pdf_path = "Baigiang-atbm-httt-2021.pdf"
    output_path = "atbm.md"
    
    convert_pdf_to_markdown(pdf_path, output_path) 