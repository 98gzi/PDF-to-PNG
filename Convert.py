from pdf2image import convert_from_path
from pathlib import Path

root = "C:/Users/eddie/OneDrive/Desktop/Testing/"

pdf_dir = Path('C:/BarTender/Candle Labels - Colour/labels_full')
save_dir = Path('C:/Users/eddie/OneDrive/Desktop/Testing/Images-Full')

for pdf_file in pdf_dir.glob('*.pdf'):
    pages = convert_from_path(pdf_file, 500, poppler_path= root + 'poppler-0.68.0/bin')
    for num, page in enumerate(pages, start=1):
        page.save(save_dir / f'{pdf_file.stem}.png', 'PNG')