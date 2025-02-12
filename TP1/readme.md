# Primeiro TPC do semestre
2025-02-07
## Resumo

### Problema
1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

### Funcionamento
O programa lê um texto e soma todos os números encontrados, mas apenas quando a contagem está ativada. A contagem começa ativa, mas pode ser desativada ao encontrar a palavra "off" e reativada ao encontrar "on".

Ele percorre cada caractere do texto, verificando se é um número. Caso seja, ele acumula-o numa variável temporária. Quando encontra um caractere que não é um número, verifica se há um valor acumulado e, se houver, soma esse número ao total.

Sempre que encontra a palavra "on", a contagem é ativada, e quando encontra "off", é desativada. Para isso, verifica a posição atual no texto e os caracteres seguintes para garantir que a palavra esteja completa. 

No final, o código imprime a soma total de todos os números que foram contabilizados enquanto a contagem estava ativa.

**Notas:**  
Assumo que é necessário ativar o modo de soma antes de considerar qualquer número, ou seja, deve haver um "on" inicial. Além disso, qualquer ocorrência de "on" ou "off" no texto será considerada, mesmo que faça parte de uma palavra maior. Isso significa que palavras como "one" serão interpretadas como um "on" válido.

## Instrução de utilização
Como não foi especificado a forma como a string em questão era fornecida, eu interpretei de forma a utilizador fornecer a linha a partir do stdin ao iniciar o programa.
