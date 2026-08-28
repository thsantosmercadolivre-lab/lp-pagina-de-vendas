# Do Carandiru ao Palácio — página de vendas

Página de vendas com VSL do livro de Ricardo Oliveira, vendido a R$ 49,90.
Arquivo principal: `do-carandiru-ao-palacio.html`, uma página só, sem build,
sem dependência. Abra direto no navegador para ver.

`pagina-de-vendas.html` e `index.html` são de outro produto (LP de serviço) e
não têm relação com esta página.

## Estrutura

Três seções, e o pedido é manter em três:

1. Hero com o player da VSL. A foto do Ricardo com a camisa da Seleção é uma
   camada atrás do player, em `mix-blend-mode: screen` com máscara dupla
   (linear no wrapper, radial na imagem) para não lavar o H1 nem o CTA.
2. O livro: mockup 3D com lombada, bola dourada por trás como ilustração,
   bullets, ficha técnica, e o carrossel de avaliações.
3. Oferta: card de preço com borda gradiente girando, 5 benefícios, garantia
   de 7 dias, rodapé. Barra fixa de preço no mobile.

## Identidade

Paleta e tipografia vêm da apresentação `OS CONVOCADOS` do Ricardo:
preto `#050505`, dourado da CBF `#ffc400`, branco. Display em Anton, texto em
Archivo, via Google Fonts. Nada de outra família sem o Thiago pedir.

Referência de layout que ele deu: `andreavermontpsicanalise.com`. O domínio é
bloqueado pela política de rede da sessão remota, então a página foi montada
no padrão de VSL brasileira, e não copiada da referência.

## Regras de escrita

O Thiago pediu explicitamente, e vale para qualquer texto novo:

- Nenhum travessão na página. Zero. Use vírgula.
- Não picotar frase em ponto final onde cabe vírgula.
- Nada de frase de efeito no lugar de argumento, nada de "não é só X, é Y",
  nada de listas com cabeçalho em negrito. Rode a skill `humanizer` antes de
  entregar copy nova.
- A copy fala do que o leitor ganha (mentalidade, foco, continuar quando bate
  vontade de largar), não da biografia em si.

## Nunca inventar prova social

As avaliações da Amazon não são alcançáveis desta sessão. Os cards do
carrossel trazem só o que deu para confirmar. Não crie nome de leitor, data,
nota média, contagem de avaliações nem fileira de estrelas sem o Thiago
mandar o print ou o texto real. Os comentários dentro do `.track` explicam
onde colar print de imagem e onde colar texto.

## Dados do livro, conferidos na capa oficial

- Subtítulo: "Eu sou um dos 15% que não desistiram", no plural.
- Prefácio de Ronaldo Fenômeno.
- Editora AD Santos, ISBN 978-65-89636-05-2.

Uma versão anterior dizia "desistiu" e "Editora Jesus", os dois estavam
errados.

## Imagens

`assets/ricardo-brasil.jpg`, `assets/ricardo-cbf.jpg`, `assets/bola-ouro.jpg`
e `assets/camisa-10.jpg` foram recortados dos slides 4K do PPTX. O fundo deles
é quase preto de origem, por isso aparecem com `mix-blend-mode: screen` sobre
o fundo escuro, em vez de recorte com alfa. Tentei matte por luminância e
ficou com buraco na jaqueta preta, não vale repetir.

`assets/livro-capa.jpg` alimenta o mockup e o fundo desfocado da página.
Para trocar pela capa oficial: `python3 trim-capa.py` (procura em ~/Downloads)
ou `python3 trim-capa.py caminho/da/capa.jpg`.

## Pendências

- [ ] Capa oficial no lugar da provisória, via `trim-capa.py`.
- [ ] URL do embed da VSL em `data-embed` na div `#vsl`.
- [ ] Link do checkout no `href` do `a[data-cta="checkout"]`.
- [ ] Prints reais das avaliações da Amazon no carrossel.
- [ ] Foto do Ricardo com a camisa do Atlético-MG, que ele mandou no chat mas
      nunca chegou como arquivo.

Os pontos de troca no HTML estão marcados com comentário.

## Antes de entregar

A página não tem teste automatizado. Confira no navegador em 1440px e em
390px: sem rolagem horizontal, sem erro no console, o carrossel indo e
voltando, e o clique no player abrindo o iframe quando `data-embed` está
preenchido.
