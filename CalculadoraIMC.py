# Calculadora de IMC Indice de Massa Corporal, desenvolvida em Python
# Desenvolvido em 23/11/2026 - Prof Luiz no Senac

# Váriaveis da Calculadora
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))

# Fórmula responsável por definir IMC
imc = peso / (altura * altura)

# Verifica e retorna o IMC e classificação
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade") 