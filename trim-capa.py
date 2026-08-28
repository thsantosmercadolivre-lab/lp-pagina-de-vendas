#!/usr/bin/env python3
"""Recorta as abas brancas da capa oficial e grava em assets/livro-capa.jpg.

    python3 trim-capa.py caminho/para/capa-original.jpg
"""
import sys
from PIL import Image, ImageChops

src = sys.argv[1] if len(sys.argv) > 1 else 'capa-original.jpg'
im = Image.open(src).convert('RGB')

# tudo acima de 244 em todos os canais conta como aba branca
mask = im.point(lambda v: 255 if v > 244 else 0).convert('L')
box = ImageChops.invert(mask).getbbox()
if box:
    im = im.crop(box)

im.save('assets/livro-capa.jpg', quality=92, optimize=True, progressive=True)
print(f'capa recortada: {im.size[0]}x{im.size[1]}  ->  assets/livro-capa.jpg')
