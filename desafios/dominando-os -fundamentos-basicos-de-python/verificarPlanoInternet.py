# Desafio

# Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

# Planos Oferecidos:

# - Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
# - Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
# - Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.
# Entrada

# Como entrada solicite o consumo médio mensal de dados em GB (float).
# Saída

# Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.

#-------------------------------------------------------------------------------------#

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo_medio_mensal):
  if consumo_medio_mensal <= 10:
    print("Plano Essencial Fibra - 50Mbps")
  elif consumo_medio_mensal >10 and consumo_medio_mensal <= 20:
    print("Plano Prata Fibra - 100Mbps")
  elif consumo_medio_mensal > 20:
    print("Plano Premium Fibra - 300Mbps")
  else:
    return
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
recomendar_plano(consumo)

