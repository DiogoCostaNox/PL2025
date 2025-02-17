file_path = "obras.csv"

def split_csv_line(line):
    parts = []
    current = []
    inside_quotes = False
    
    for char in line:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == ';' and not inside_quotes:
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    
    parts.append("".join(current).strip())
    return parts

def read_complete_lines(file):
    complete_line = ""
    inside_quotes = False
    
    for raw_line in file:
        line = raw_line.strip()
        complete_line += (" " if complete_line else "") + line 
        
        inside_quotes ^= line.count('"') % 2  
        
        if not inside_quotes:
            yield complete_line
            complete_line = ""
    
    if complete_line:
        yield complete_line

compositores = set()
distribuicao_obras = {}
obras_por_periodo = {}

with open(file_path, "r", encoding="utf-8") as file:
    header = next(file).strip()
    header_parts = split_csv_line(header)
    
    idx_nome = header_parts.index("nome")
    idx_periodo = header_parts.index("periodo")
    idx_compositor = header_parts.index("compositor")
    
    for line in read_complete_lines(file):
        campos = split_csv_line(line.strip())
        if len(campos) < max(idx_nome, idx_periodo, idx_compositor) + 1:
            continue  
        
        nome = campos[idx_nome].strip()
        periodo = campos[idx_periodo].strip()
        compositor = campos[idx_compositor].strip()
        
        compositores.add(compositor)
        
        distribuicao_obras[periodo] = distribuicao_obras.get(periodo, 0) + 1
        
        if periodo not in obras_por_periodo:
            obras_por_periodo[periodo] = []
        obras_por_periodo[periodo].append(nome)

todos_compositores = sorted(compositores)
for periodo in obras_por_periodo:
    obras_por_periodo[periodo].sort()

with open("compositores.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(todos_compositores))

with open("distribuicao_obras.txt", "w", encoding="utf-8") as f:
    for periodo, quantidade in sorted(distribuicao_obras.items()):
        f.write(f"{periodo}: {quantidade}\n")

with open("obras_por_periodo.txt", "w", encoding="utf-8") as f:
    for periodo, obras in sorted(obras_por_periodo.items()):
        f.write(f"{periodo}:\n" + "\n".join(obras) + "\n\n")
