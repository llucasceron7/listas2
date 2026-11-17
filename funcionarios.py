funcionarios = [
    [1, "Maycon", "Gerente Administrativo", 7000],
    [2, "Matias", "Auxiliar Administrativo", 2500],
    [3, "Henrique", "Coordenador do curso", 5000]
]

print(funcionarios)

funcionarios.append([4, "Ana Silva", "Analista", 4500])
funcionarios.append([5, "Carlos Souza", "Desenvolvedor", 5800])

for funcionario in funcionarios:
    print(f"ID: {funcionario[0]} | Nome: {funcionario[1]} | Cargo: {funcionario[2]} | Salário: R$ {funcionario[3]:.2f}")


