# Analisador Léxico em Python
2025-03-17

## Resumo

### Problema
1. Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases

### Processamento do Texto
- O código lê um arquivo de entrada linha por linha e, usando expressões regulares, identifica e extrai os tokens definidos.
- Cada linha é processada e os tokens são identificados, classificados e armazenados em uma lista de objetos `Token`.
- A cada token encontrado, o tipo, o valor, a linha e a posição do token são armazenados.
- A saída é gerada em um arquivo de texto, onde cada linha contém a representação do token.

### Métodos Utilizados
- **Expressões regulares** para identificar padrões no texto e associá-los aos tipos de tokens.
- **Classe `Token`** para encapsular as informações dos tokens (tipo, valor, linha, posição).
- **Função `analisa_linha`** que processa cada linha do arquivo e retorna os tokens encontrados.
- **Função `main`** para coordenar a leitura do arquivo de entrada, chamar o analisador e escrever o resultado no arquivo de saída.

### Output
- O código gera um arquivo `resultado.txt`, contendo os tokens identificados no arquivo de entrada. Cada token é representado na forma:
    ```
    <TIPO> => "<VALOR>" (L:<LINHA>, C:<POSIÇÃO>)
    ```

### Resultados
1. **Identificação precisa de tokens**: Números, palavras, variáveis, e outros tokens definidos.
2. **Armazenamento de tokens com detalhes**: Linha e posição dos tokens no arquivo original.
3. **Geração de um arquivo de saída legível**: Tokens são claramente apresentados, incluindo tipo e valor.