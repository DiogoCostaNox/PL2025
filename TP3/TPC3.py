import re

def convert_list(match):
        items = match.group(1).split('\n')
        items = [f'<li>{item[3:]}</li>\n' for item in items if item]
        return '<ol>\n' + ''.join(items) + '</ol>\n'

def markdown_to_html(md_text):
    # Cabeçalhos
    md_text = re.sub(r'### (.+)', r'<h3>\1</h3>', md_text)
    md_text = re.sub(r'## (.+)', r'<h2>\1</h2>', md_text)
    md_text = re.sub(r'# (.+)', r'<h1>\1</h1>', md_text)
    
    # Bold
    md_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', md_text)
    
    # Itálico
    md_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', md_text)
    
    # Listas numeradas
    md_text = re.sub(r'((?:\d+\. .+\n?)+)', convert_list, md_text)
    
    # Links
    md_text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', md_text)
    
    # Imagens
    md_text = re.sub(r'!\[(.*?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', md_text)
    
    return md_text

# Exemplo de uso
md_example = """# Título Principal
## Subtítulo
### Sub-subtítulo

Este é um **exemplo** de *Markdown*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt).

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)"""

html_result = markdown_to_html(md_example)
print(html_result)