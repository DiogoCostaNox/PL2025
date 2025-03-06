# Terceiro TPC do Semestre
2025-02-27

## Resumo

### Problema
1. Criar um programa em Python que converta texto em formato Markdown para HTML.
2. O conversor deve suportar os seguintes elementos da "Basic Syntax" do Markdown:
    - Cabeçalhos (`#`, `##`, `###`)
    - Negrito (`**texto**`)
    - Itálico (`*texto*`)
    - Listas numeradas (`1. item`)
    - Links (`[texto](URL)`)
    - Imagens (`![alt](URL)`).

### Processamento do Markdown
- O código recebe um texto em formato Markdown e processa cada linha usando expressões regulares para converter os elementos suportados em HTML.
- As substituições são feitas na seguinte ordem:
    1. **Cabeçalhos**: Converte `#`, `##` e `###` para `<h1>`, `<h2>` e `<h3>`.
    2. **Negrito**: Transforma `**texto**` em `<b>texto</b>`.
    3. **Itálico**: Converte `*texto*` para `<i>texto</i>`.
    4. **Listas numeradas**: Identifica blocos de listas numeradas e os transforma em `<ol><li>item</li></ol>`.
    5. **Links**: Substitui `[texto](URL)` por `<a href="URL">texto</a>`.
    6. **Imagens**: Converte `![alt](URL)` em `<img src="URL" alt="alt"/>`.

### Métodos Utilizados
- **Expressões regulares (`re.sub`)** para reconhecer e substituir os elementos do Markdown por suas versões em HTML.
- **Função auxiliar para listas numeradas**, garantindo que múltiplos itens sejam corretamente encapsulados em `<ol>` e `<li>`.

### Output
- O código retorna uma string contendo o HTML formatado equivalente ao Markdown fornecido.
- Pode ser utilizado para converter arquivos `.md` diretamente em `.html`.

### Resultados
1. **Conversão precisa dos principais elementos do Markdown para HTML.**
2. **Estrutura correta das listas numeradas em HTML.**
3. **Manutenção da formatação de negrito, itálico, links e imagens.**

