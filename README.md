# lp-pagina-de-vendas

Páginas de vendas estáticas, um arquivo HTML por página, sem build.

| Arquivo | O que é |
| --- | --- |
| `do-carandiru-ao-palacio.html` | Página com VSL do livro do Ricardo Oliveira |
| `pagina-de-vendas.html` | LP do serviço de página de vendas em 72h |
| `assets/` | Imagens usadas pela página do livro |
| `trim-capa.py` | Recorta as abas brancas da capa e grava em `assets/livro-capa.jpg` |

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

- `data-embed` na div `#vsl`, com a URL do embed da VSL
- `href` do link `data-cta="checkout"`, com a URL do checkout
- os cards do carrossel de avaliações, para colar os prints da Amazon

## Contexto para o Claude Code

`CLAUDE.md` guarda a identidade visual, as regras de escrita e as pendências.
Uma sessão do Claude Code aberta nesta pasta carrega esse arquivo sozinha.
