palavras = ('Aprender', 'Programar', 'Linguagem', 'Python')

for x in palavras:
    print(f'\nNa palavra {x} temos ', end=' ')
    for letra in x:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')