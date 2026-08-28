#!/usr/bin/env python3
"""Recorta as abas brancas da capa oficial e grava em assets/livro-capa.jpg.

Uso:
    python3 trim-capa.py                      # procura a capa em ~/Downloads
    python3 trim-capa.py caminho/da/capa.jpg  # usa o arquivo que você apontar

A capa alimenta o mockup 3D e o fundo desfocado da página, os dois apontam
para assets/livro-capa.jpg, então trocar esse arquivo atualiza a página toda.
"""
import glob
import os
import sys

from PIL import Image, ImageChops

AQUI = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(AQUI, 'assets', 'livro-capa.jpg')
EXTS = ('jpg', 'jpeg', 'png', 'webp', 'bmp', 'tif', 'tiff')


def achar_capa():
    """Procura a capa baixada da Amazon na pasta Downloads."""
    downloads = os.path.expanduser('~/Downloads')
    achados = []
    for ext in EXTS:
        achados += glob.glob(os.path.join(downloads, f'*{ext}'))
        achados += glob.glob(os.path.join(downloads, f'*{ext.upper()}'))
    # o nome do arquivo da Amazon começa com o ID da imagem
    amazon = [f for f in achados if os.path.basename(f).startswith('61Dshqk')]
    candidatos = amazon or achados
    if not candidatos:
        return None
    return max(candidatos, key=os.path.getmtime)


def recortar(im, limite=244):
    """Remove as bordas claras uniformes ao redor da capa."""
    mascara = im.point(lambda v: 255 if v > limite else 0).convert('L')
    caixa = ImageChops.invert(mascara).getbbox()
    return im.crop(caixa) if caixa else im


def main():
    origem = sys.argv[1] if len(sys.argv) > 1 else achar_capa()
    if not origem:
        sys.exit('Não achei nenhuma imagem em ~/Downloads. '
                 'Passe o caminho: python3 trim-capa.py caminho/da/capa.jpg')
    if not os.path.isfile(origem):
        sys.exit(f'Arquivo não encontrado: {origem}')

    im = Image.open(origem).convert('RGB')
    antes = im.size
    im = recortar(im)

    if im.size == antes:
        print('Nenhuma aba branca encontrada, a imagem já estava no corte.')

    os.makedirs(os.path.dirname(DESTINO), exist_ok=True)
    im.save(DESTINO, quality=92, optimize=True, progressive=True)
    print(f'origem : {origem}')
    print(f'antes  : {antes[0]}x{antes[1]}')
    print(f'depois : {im.size[0]}x{im.size[1]}')
    print(f'gravado: {os.path.relpath(DESTINO, AQUI)}')
    print('\nAbra do-carandiru-ao-palacio.html no navegador para conferir.')


if __name__ == '__main__':
    main()
