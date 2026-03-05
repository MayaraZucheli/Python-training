f = input('Digite uma frase: ').strip().upper().replace(" ", "")
print(f"A letra A aparece {f.upper().count('A')} vezes na frase.")
print(f"A primeira letra A aparece na posição {f.upper().find('A') + 1}")
print(f"A última letra A aparece na posição {f.upper().rfind('A') + 1}")