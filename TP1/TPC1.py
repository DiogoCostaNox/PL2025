import sys

def ler_texto():
    input = sys.stdin.read
    
    total = 0
    enable = True
    number = ""

    texto = input()  

    i = 0
    while i < len(texto):
        char = texto[i]

        if enable:
            if char.isdigit():
                number += char
            elif number:
                total += int(number)
                number = ""

        if char.lower() == 'o':
            if i + 1 < len(texto) and texto[i + 1].lower() == "n":
                enable = True
            elif i + 2 < len(texto) and texto[i + 1].lower() == "f" and texto[i + 2].lower() == "f":
                enable = False
                i += 2  

        i += 1

    if number:
        total += int(number)

    return total

if __name__ == "__main__":
    total = ler_texto()
    print(total)