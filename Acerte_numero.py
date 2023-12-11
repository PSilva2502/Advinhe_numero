print('------------Jogo do advinha o numero------------')
import random

numero_aleatorio = random.randint(1, 100)
acerto = False

while acerto == False:
  numero_usuario = int(input("Digite um número: "))
  if numero_usuario < numero_aleatorio:
    print('O número digitado é menor que o número aleatório')
  elif numero_usuario > numero_aleatorio:
    print('Número digitado é maior que o número aleatório')
  elif numero_usuario == numero_aleatorio:
    acerto = True
    print('Voce acertou o número aleatório')