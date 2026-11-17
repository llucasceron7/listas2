livros = [
    [1, "Hábitos Atômicos", "James Clear", 2018],
    [2, "O Poder do Hábito", "Charles Duhigg", 2012],
    [3, "Como fazer amigos e influenciar pessoas", "Dale Carnegie", 1936]
]

print("Autor:", livros[1][2])
for id_livro, titulo, autor, ano in livros:
    print(f'ID: {id_livro} | O livro "{titulo}" foi escrito por {autor} em {ano}.')

livros[0][3] = 2024
print(livros)

titulo_procurado = "Hábitos"
encontrado = False

for livro in livros:
    if livro[1] == titulo_procurado:
        print("Livro localizado!", livro)
        encontrado = True
        break
    
if encontrado == False:
    print("Livro não encontrado")

id_remover = 2
for indice, livro in enumerate(livros):
    if livro[0] == id_remover:
        removido = livros.pop(indice)
        print("Registro removido:", removido)
        break