import re
from pathlib import Path

text = Path(r'C:\Users\ly182\AppData\Local\Temp\flourish-source.html').read_text(encoding='utf-8')
pattern = re.compile(r'"filter":"Spectrum","label":"([^"]+)".*?"value":\["([^"]+)"\]')
items = [(label, float(value)) for label, value in pattern.findall(text)]
for label, value in sorted(items, key=lambda item: item[1], reverse=True)[:15]:
    print(f'{label}: {value:.6f}')
