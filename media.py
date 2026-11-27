# Calculadora de Média de 4 notas de um aluno, e retorna "Aprovado" ou "Reprovado"
# Desenvolvido em 27/11/26 - Prof Luiz Gustavo - Senac

# Declarando váriaveis da calculadora
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))
nota3 = float(input("insira a terceira nota: "))
nota4 = float(input("insira a quarta nota: "))

# Calcula a média e atribui a váriavel "media"
media = float((nota1 + nota2 + nota3 + nota4) / 4)

# Exibe o resultado da média
print("A média das notas é: ", media)