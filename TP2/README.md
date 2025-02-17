# Segundo TPC do semestre
2025-02-16

## Resumo 

### Problema
1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

### Leitura do Arquivo CSV
- O código abre um arquivo CSV chamado "obras.csv" e lê suas linhas, dividindo os campos de cada linha com um delimitador `;`.
- A função `split_csv_line` divide uma linha do CSV em partes, respeitando as aspas.

### Processamento das Linhas
- A função `read_complete_lines` lê o arquivo e trata linhas que podem estar mal formatadas por causa das aspas. Tive que criar a função porque ao respeitar as aspas acabou por dar este erro.

### Extração e Organização dos Dados
- O código identifica e armazena os índices dos campos de interesse (`nome`, `periodo`, `compositor`) a partir do cabeçalho do CSV, uma vez que são os únicos necessários à realização do exercício.
- Usa conjuntos e dicionários para agrupar e contar as obras:
    - `compositores`: Um conjunto de todos os compositores.
    - `distribuicao_obras`: Um dicionário que conta o número de obras por período.
    - `obras_por_periodo`: Um dicionário onde cada período tem uma lista das obras correspondentes.

### Geração dos Resultados
- Escreve a lista ordenada de compositores em "compositores.txt".
- Escreve a distribuição das obras por período em "distribuicao_obras.txt".
- Escreve as obras organizadas por período em "obras_por_periodo.txt".

### Resultados
1. **Lista ordenada alfabeticamente dos compositores musicais.**
2. **Distribuição das obras por período: quantas obras catalogadas em cada período.**
3. **Dicionário em que a cada período está associada uma lista alfabética dos títulos das obras desse período.**
