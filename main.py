from pathlib import Path
from docling.document_converter import DocumentConverter 


INPUT_FILE = Path('Sample.pdf')
OUTPUT_FILE = Path('output.md')

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f'File not found: {INPUT_FILE}')

    converter = DocumentConverter()

    result = converter.convert(str(INPUT_FILE))

    #print(result)
    document = result.document

    markdown = document.export_to_markdown()

    OUTPUT_FILE.write_text(markdown, encoding="utf-8")

    print(f'converted: {INPUT_FILE}')
    print(f'Output: {OUTPUT_FILE}')
    print(f'\nPreview \n')
    print(markdown[:2000])    




if __name__ == "__main__":
    main()