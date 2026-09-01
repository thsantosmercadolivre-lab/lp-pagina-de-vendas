# lp-pagina-de-vendas

Páginas de vendas estáticas, um arquivo HTML por página, sem build.

| Arquivo | O que é |
| --- | --- |
| `do-carandiru-ao-palacio.html` | Página com VSL do livro do Ricardo Oliveira |
| `pagina-de-vendas.html` | LP do serviço de página de vendas em 72h |
| `assets/` | Imagens usadas pela página do livro |
| `trim-capa.py` | Recorta as abas brancas da capa e grava em `assets/livro-capa.jpg` |

## Colocar o vídeo da VSL

O player procura por `assets/vsl.mp4`. Basta colocar o arquivo lá:

```bash
mv ~/Downloads/SEU-VIDEO.mp4 assets/vsl.mp4
```

Se preferir hospedar num player externo (VTurb, Panda, YouTube, Vimeo),
preencha `data-embed` na div `#vsl`, que ele passa na frente do arquivo.

## Ver a página

Abra o arquivo `.html` direto no navegador. Se preferir servir:

```bash
python3 -m http.server 8000
# depois acesse http://localhost:8000/do-carandiru-ao-palacio.html
```

## Trocar a capa do livro

A capa aparece em dois lugares, o mockup 3D e o fundo desfocado da página, e
os dois leem o mesmo arquivo. Para trocar:

```bash
pip install pillow          # só na primeira vez
python3 trim-capa.py        # procura a capa em ~/Downloads
```

Ou apontando o arquivo:

```bash
python3 trim-capa.py ~/Downloads/capa.jpg
```

O script remove as bordas brancas e grava em `assets/livro-capa.jpg`.

## O que ainda falta preencher

Dentro de `do-carandiru-ao-palacio.html`, procure pelos comentários:

- o vídeo da VSL em `assets/vsl.mp4` (o player já aponta para lá)
- os cards do carrossel de avaliações, para colar os prints da Amazon
- a capa oficial, via `trim-capa.py`

O checkout já está ligado no `https://pay.kiwify.com.br/BAA9Xsp`.

## Contexto para o Claude Code

`CLAUDE.md` guarda a identidade visual, as regras de escrita e as pendências.
Uma sessão do Claude Code aberta nesta pasta carrega esse arquivo sozinha.
